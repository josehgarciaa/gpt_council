"""
ford begin_TODO
- Rename the "history" attribute to "messages_history" or simply "messages" for clarity.
- Consider renaming "append_message" to "add_message" for consistency with common naming conventions.
- Clarify the expected types in the type hint for the "message" parameter in append_message (e.g., include APIResponse and ClientAction as well).
- Ensure that the exception message in append_message clearly indicates which type is expected.
end_todo

Module: chat_manager.history_manager
Description:
    This module handles the chat history, storing all chat messages in a
    format that can be easily processed by other classes and functions in
    the application. The ChatHistory class provides methods to append new
    messages and to retrieve the entire conversation history in an API-
    compatible format.
    
Classes:
    ChatHistory:
        A data class that maintains a list of messages. It provides methods
        for appending individual or multiple messages and for retrieving the
        complete chat history.
"""

from dataclasses import dataclass, field
from typing import List, Union, Iterable
from chat_manager import APIResponse, ChatUserMessage, ClientAction, ChatDeveloperMessage


@dataclass
class ChatHistory:
    """
    Stores the history of chat messages, allowing messages to be appended
    and retrieved in an API-compatible format.
    
    Attributes:
        history (List[dict]): A list that stores messages as dictionaries.
    """
    history: List[dict] = field(default_factory=list)

    def append_message(self, message: Union[ChatUserMessage, APIResponse, ClientAction]) -> None:
        """
        Appends a message or a collection of messages to the chat history.
        
        Depending on the type of the message, this method retrieves the API-
        compatible message(s) and adds them to the history.
        
        Args:
            message (Union[ChatUserMessage, APIResponse, ClientAction]): A single
                message instance or an object providing the 'get_api_message()' method.
        
        Raises:
            AttributeError: If the provided object does not have a 'get_api_message()'
                method.
        """
        if isinstance(message, (ChatUserMessage,ChatDeveloperMessage, APIResponse)):
            # Single message case.
            self.history.append(message.get_api_message())
        elif isinstance(message, ClientAction):
            # Handle multiple messages.
            for api_message in message.get_api_message():
                self.history.append(api_message)
        else:
            raise AttributeError(f"Object {message} does not have 'get_api_message()' method.")

    def messages(self) -> List[dict]:
        """
        Retrieves the entire chat history.
        
        Returns:
            List[dict]: A list of messages formatted as API-compatible dictionaries.
        """
        return self.history
    
    def clear_messages(self):
        print("deleting history")
        self.history = []
