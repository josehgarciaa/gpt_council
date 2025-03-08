"""
ford begin_TODO
- Avoid using wildcard imports to prevent namespace pollution; consider explicit imports.
- Ensure consistency in naming conventions across submodules (e.g., consider renaming ChatUserMessage to ChatUserMessageHandler).
- Consider renaming "handler" to "chat_manager_facade" for better clarity.
end_todo

Module: chat_manager
Version: 1.0.0

Description:
    The chat_manager module serves as the central component for managing chat interactions
    between the client and the server. It aggregates various submodules responsible for processing
    user messages, handling API responses, managing chat history, and executing client actions.

Submodules:
    - chat_user_message: Processes and prepares user messages for the chat system.
    - api_response: Handles raw API responses, determines necessary follow-up actions, and converts responses
      into internal formats.
    - client_action: Executes actions on the client side based on API responses and model tool calls.
    - history_manager: Manages the storage and retrieval of the complete chat history.
    - handler: Provides the ChatManager facade for orchestrating the overall chat interactions.
"""

from .chat_user_message import *
from .chat_developer_message import *
from .api_response import *
from .client_action import ClientAction
from .history_manager import ChatHistory
from .handler import ChatManager
