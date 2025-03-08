"""
ford begin_TODO
- Consider renaming class 'ClientAction' to 'ClientActionHandler' for clarity.
- Rename method 'get_api_message' to 'get_api_messages' to indicate it returns a list.
- Rename method 'required' to 'is_action_required' for improved readability.
- Consider adding type hints for method parameters and return types.
end_todo

Module: chat_manager.client_action
Description:
    This module handles client actions required by the chat manager.
    It processes API responses to determine if any client actions are needed,
    and coordinates the creation of action messages using model tool invocations.
"""

from chat_manager import APIResponse
import json

class ClientAction():
    """
    Handles client actions as part of the chat management system.

    This class is responsible for processing API responses to extract
    tool calls, executing those calls via the model's tools, and maintaining
    a list of API messages to be sent back to the client.
    """
    
    def __init__(self):
        """
        Initializes a new instance of ClientAction with an empty list of API messages.
        """
        self.api_messages = []

    def get_api_message(self):
        """
        Retrieve the list of API messages that have been generated.

        Returns:
            list: The list of API messages.
        """
        return self.api_messages
                     
    def required(self, api_response):
        """
        Check if a client action is required based on the API response.

        Args:
            api_response (APIResponse): The APIResponse object containing the response data.

        Returns:
            bool: True if a client action is required, otherwise False.
        """
        return api_response.required_action()
    
    def execute(self, model, api_response):
        """
        Execute client actions based on tool calls found in the API response.

        For each tool call in the API response, this method retrieves the
        corresponding tool from the model, calls it with the provided arguments,
        and constructs an API message which is then appended to the internal list.

        Args:
            model: The model object containing the tools list.
            api_response: The APIResponse object with raw response data.

        Returns:
            bool: True after processing the tool calls.
        """
        for tool_call in api_response.raw_api_response.choices[0].message.tool_calls:
            api_message = {"role": "tool", "tool_call_id": tool_call.id, "content": ""}
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            api_message["content"] = str(model.tools_list.get_tool_by_name(function_name).call_function(function_args))
            self.api_messages.append(api_message)
        return True 
