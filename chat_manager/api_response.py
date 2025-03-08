"""
ford begin_TODO
- Consider renaming class 'APIResponse' to 'ApiResponse' for consistency.
- Rename attribute 'call_api_value' to 'should_call_api' for clarity.
- Rename attribute 'call_tool_value' to 'requires_tool_call' for clarity.
- Rename method 'readable' to 'get_readable_message' to be more descriptive.
- Rename method 'handle' to 'handle_response' to clarify its purpose.
- Add type hints for method parameters and return types.
end_todo

Module: chat_manager.api_response
Description:
    This module handles raw API responses from the chat client.
    It determines whether further API calls are needed or if specific
    client actions should be executed. It also processes the raw API
    response into internal structures such as plain text or a structured
    API response.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict
from openai.types.chat import ChatCompletionMessageParam
import json

class APIResponse():
    """
    A class for processing API responses within the chat manager.

    This class analyzes raw API responses to determine if additional API
    calls or client actions (e.g., tool invocations) are required. It also
    converts the raw API response into a human-readable format.
    """
    
    def __init__(self):
        """
        Initialize an APIResponse instance with default state.

        Attributes:
            message: Holds the API message (initially None).
            call_api_value (bool): Flag indicating whether an API call should be made.
            processed_content: The processed, human-readable content.
            raw_api_response: The raw response data from the API.
            call_tool_value (bool): Flag indicating whether a tool call is required.
        """
        self.message = None
        self.call_api_value = True 
        self.processed_content = None
        self.raw_api_response = None
        self.call_tool_value = False 

    def call_api(self):
        """
        Check if an API call should be performed based on the response state.

        Returns:
            bool: True if an API call is needed, otherwise False.
        """
        return self.call_api_value

    def get_api_message(self):
        """
        Extract and return the API message from the raw API response.

        Returns:
            The API message from the first choice in the raw API response.
        """
        return self.raw_api_response.choices[0].message       
        

    def readable(self):
        """
        Convert the raw API response into a human-readable string.

        The method concatenates the role and content from the API message.

        Returns:
            str: A formatted string representing the API message.
        """
        message = self.raw_api_response.choices[0].message
        self.processed_content = "role: " + message.role + "\n" + message.content
        return self.processed_content

    def required_action(self):
        """
        Determine if a client action (e.g., a tool call) is required.

        Returns:
            bool: True if a tool call is required, otherwise False.
        """
        return self.call_tool_value
             
     
    def handle(self, raw_api_response):
        """
        Process the raw API response and update the internal state accordingly.

        This method sets the raw API response, checks for tool call indications,
        and updates flags to indicate whether further API calls or client actions
        are needed.

        Args:
            raw_api_response: The raw API response data to be processed.

        Returns:
            Either the original raw API response (if tool calls are detected) or
            the updated APIResponse instance.
        """
        self.raw_api_response = raw_api_response
        
        if self.raw_api_response.choices[0].message.tool_calls is not None:
            self.call_tool_value = True                
            self.call_api_value = True
            return raw_api_response                                    
        
        self.call_tool_value = False                
        self.call_api_value = False
        self.raw_api_response = raw_api_response        
        return self
