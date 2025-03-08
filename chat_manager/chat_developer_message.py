"""
ford begin_TODO
- Rename class "ChatUserMessage" to "ChatUserMessageHandler" to clarify its responsibility.
- Rename attribute "api_compatible_message" to "api_message" for brevity and clarity.
- Rename attribute "readable_content" to "plain_text_message" to better indicate its purpose.
- Rename method "handle" to "process_message" to better reflect the action performed.
- Rename method "readable" to "get_readable_message" to be more descriptive.
end_todo

Module: chat_manager.chat_user_message
Description:
    This module handles user messages before they are sent to the chat controller.
    It preprocesses raw text messages into formats that are compatible with the API as well
    as human-readable text for internal processing.
"""

from openai.types.chat import ChatCompletionDeveloperMessageParam 


class ChatDeveloperMessage:
    """
    Handles user messages before sending them to the chat controller.
    Performs preprocessing of raw text messages to generate both an API-compatible
    message and a human-readable message format.

    Attributes:
        api_compatible_message (ChatCompletionMessageParam): The processed message
            formatted for the chat server's API.
        readable_content (str): A human-readable version of the message.
    """

    def __init__(self) -> None:
        """
        Initializes an empty ChatUserMessage instance with default values.
        """
        self.api_compatible_message = None    
        self.readable_content = None     

    def handle(self, content: str) -> "ChatDeveloperMessage":
        """
        Processes the input message content and stores it as an API-compatible message.

        Args:
            content (str): The raw text message from the user.

        Returns:
            ChatUserMessage: The instance with the processed API-compatible message.
        """
        # More preprocessing can be added in future implementations.
        self.api_compatible_message = ChatCompletionDeveloperMessageParam(
            role="developer", content=content
        )

        return self

    def get_api_message(self) -> ChatCompletionDeveloperMessageParam:
        """
        Retrieves the API-compatible message.

        Returns:
            ChatCompletionDeveloperMessageParam: The processed message formatted for the API.
        """
        return self.api_compatible_message

    def readable(self) -> str:
        """
        Generates a human-readable version of the API-compatible message.

        Returns:
            str: A formatted string containing the role and content of the message.
        """
        message = self.api_compatible_message
        self.readable_content = "role:" + message.get("role") + "\n" + message.get("content")
        return self.readable_content
