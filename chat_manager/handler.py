"""
ford begin_TODO
- Consider renaming class "ChatManager" to "ChatManagerFacade" for clearer intent.
- In the __init__ docstring, update parameter names to match the actual parameter ("authenticator" instead of "auth").
- Improve the return value documentation in the send_message method (e.g., "True if the message was processed successfully, False otherwise").
- Replace print statements with proper logging for production-level error reporting.
- Add type hints for the "chatbot" parameter in get_response for better clarity.
- Clarify exception handling in get_response (avoid using raise print(...)).
end_todo

Module: chat_manager.handler
Description:
    The ChatManager module serves as the facade for handling chat interactions.
    It is responsible for sending user messages to the client, capturing responses,
    and delegating the processing of these responses to appropriate internal structures
    and classes (such as ChatUserMessage, APIResponse, ChatHistory, and ClientAction).

Classes:
    ChatManager:
        A facade that orchestrates the processing of user messages and responses.
        It integrates authentication services, maintains conversation history,
        and coordinates client actions based on API responses.

Usage:
    The ChatManager is initialized with an authentication service and provides methods
    to send messages and retrieve responses from the chat client. It also supports
    clearing the conversation history if needed.
"""

from authentication import AuthenticationService
from chat_manager import ChatUserMessage, ChatDeveloperMessage, APIResponse, ChatHistory, ClientAction

class ChatManager:
    """
    A facade for managing chat interactions, authentication, and monitoring.

    This class does not maintain stateful ModelConfig or Model objects; instead,
    these are expected to be passed dynamically with each request. This design
    enhances flexibility and avoids unnecessary state management.
    """

    def __init__(self, authenticator: AuthenticationService) -> None:
        """
        Initializes the ChatManager with an authentication service and sets up
        the conversation history.

        Args:
            authenticator (AuthenticationService): Handles authentication for API requests.
        """
        self.auth = authenticator
        # self.monitor = monitor  # Monitoring service can be added if needed.
        self.chat_history = ChatHistory()  # Structured message storage.
        self.developer_message = ""


    def send_developer(self, user_text: str) -> bool:
        """
        Processes the user's message, stores it internally, and returns a status.

        The method preprocesses the raw user text into an API-compatible message
        using ChatUserMessage and appends it to the chat history.

        Args:
            user_text (str): The text input from the user.

        Returns:
            bool: True if the message was processed and stored successfully;
                  False otherwise.
        """
        try:
            developer_message = ChatDeveloperMessage().handle(user_text)
            self.chat_history.append_message(developer_message)
            return True
        except Exception:
            raise"The user message could not be processed"



    def send_message(self, user_text: str) -> bool:
        """
        Processes the user's message, stores it internally, and returns a status.

        The method preprocesses the raw user text into an API-compatible message
        using ChatUserMessage and appends it to the chat history.

        Args:
            user_text (str): The text input from the user.

        Returns:
            bool: True if the message was processed and stored successfully;
                  False otherwise.
        """
        try:
            user_message = ChatUserMessage().handle(user_text)
            self.chat_history.append_message(user_message)
            return True
        except Exception:
            print("The user message could not be processed")
            return False

    def get_response(self, chatbot) -> APIResponse:
        """
        Processes an incoming chat message and determines an appropriate response.

        This method expects a tuple containing a model configuration and a model.
        It then continuously checks if further responses are needed by calling
        the API via the authentication service's client. The method also handles
        client actions as required and updates the conversation history accordingly.

        Args:
            chatbot: A tuple (model_config, model) where:
                - model_config: Contains configuration parameters for the API call.
                - model: Contains model-specific attributes, such as model_type and tools_list.

        Returns:
            APIResponse: A readable representation of the final API response.
        """
        model_config, model = chatbot          
        api_response = APIResponse() 
        print("sending a message with model", model.model_type)
        # Check if more responses are necessary.
        while api_response.call_api():
            # Determine the actions to take based on the API response.
            raw_api_response = self.auth.get_client().chat.completions.create(
                model=model.model_type,
                messages=self.chat_history.messages(),
                tools=model.tools_list.get_all_schemas(),
                **(model_config.get_params())
            )
            # Handle the response.
            try:
                api_response.handle(raw_api_response)
            except Exception:
                raise print("Problem handling API response")
            self.chat_history.append_message(api_response)

            # Determine if the API required a client action.
            client_action = ClientAction()
            if client_action.required(api_response):
                try:
                    client_action.execute(model, api_response)
                except Exception:
                    print("Problem executing client action")
                    raise
                self.chat_history.append_message(client_action)

            print(self.chat_history.messages)

        return api_response.readable()

    def clear_history(self) -> None:
        """
        Clears the developer message and (optionally) the conversation history.

        Note:
            The method to clear chat_history messages is currently commented out.
        """
        self.chat_history.clear_messages()
