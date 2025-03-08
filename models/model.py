"""
ford begin_TODO
- Rename references to "administrator" in docstrings to "developer" to match the attribute name.
- Update the docstring for set_model_type to correctly describe its purpose.
- Consider consolidating or clarifying the usage of "tools" vs. "tools_list" attributes.
- Ensure parameter names in docstrings match those in method signatures.
end_todo

Module: models.model
Description: Defines a builder-style Model class following a director design pattern.
This module stores the configuration for a model including its inputs, outputs, and the
parameters for generating outputs based on the selected model_type. The corresponding
ModelDirector (defined in model_director.py) uses this configuration to properly set up
and control the model.
"""

from typing import Any, Dict, List, Optional
from tools import ModelTool, ModelToolList


class Model:
    """
    A builder-style class for configuring model parameters such as output types,
    streaming options, and more. Each setter returns the current instance to
    support fluent (chained) method calls.
    """

    def __init__(self) -> None:
        """
        Initialize default values for all configurable fields.
        These defaults can be overridden by calling the provided setter methods.
        """
        self.developer: str = "You are a useful assistant"
        self.model_type: str = "gpt-4o-mini"
        self.modalities: Optional[List[str]] = ["text"]
        self.audio: Optional[Dict[str, Any]] = None
        self.response_format: Optional[Dict[str, Any]] = None
        self.stream: bool = False
        self.stream_options: Optional[Dict[str, Any]] = None
        self.tools: Optional[List[Any]] = None  # Note: This attribute is currently unused.
        self.parallel_tool_calls: bool = True
        self.user: str = ""
        self.tools_list: Optional[ModelToolList] = None
        self.tools_schema = None

    def set_developer_instruction(self, developer: str) -> "Model":
        """
        Set the developer identifier for this model configuration.

        Args:
            developer (str): The developer or owner responsible for this model.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.developer = developer
        return self

    def set_model_type(self, model_type: str) -> "Model":
        """
        Set the model type for this model configuration.

        Args:
            model_type (str): The type of the model (e.g., 'gpt-4o-mini').

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.model_type = model_type
        return self

    def set_modalities(self, modalities: List[str]) -> "Model":
        """
        Specify one or more output modalities the model should generate.
        Typical values could be ["text"] or ["text", "audio"].

        Args:
            modalities (List[str]): A list of desired output modalities.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.modalities = modalities
        return self

    def set_audio(self, audio: Dict[str, Any]) -> "Model":
        """
        Provide configuration for audio output parameters.

        Args:
            audio (Dict[str, Any]): A dictionary with audio-related configuration,
                                    e.g., codec or audio format settings.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.audio = audio
        return self

    def set_response_format(self, response_format: Dict[str, Any]) -> "Model":
        """
        Specify the desired output format (e.g., JSON schema).

        Args:
            response_format (Dict[str, Any]): A dictionary defining the output format.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.response_format = response_format
        return self

    def set_stream(self, stream: bool) -> "Model":
        """
        Toggle streaming mode for partial token outputs in real time.

        Args:
            stream (bool): True to enable streaming, False otherwise.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.stream = stream
        return self

    def set_stream_options(self, stream_options: Dict[str, Any]) -> "Model":
        """
        Configure additional streaming options.

        Args:
            stream_options (Dict[str, Any]): A dictionary with stream-related parameters.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.stream_options = stream_options
        return self

    def set_tool(self, external_tool: object) -> "Model":
        """
        Add a tool to the model's list of callable tools.

        Args:
            external_tool (object): A tool (function or callable) to be added.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        if self.tools_list is None:
            self.tools_list = ModelToolList()

        self.tools_list.add_tool(ModelTool().set_function(external_tool))
        return self

    def set_tools(self, external_tools: List[object]) -> "Model":
        """
        Add a list of tools to the model's list of callable tools.

        Args:
            external_tools (List[object]): A list of tools (functions or callables) to be added.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        if self.tools_list is None:
            self.tools_list = ModelToolList()

        for external_tool in external_tools:
            self.set_tool(external_tool)
        return self

    def enable_parallel_tool_calls(self, enable: bool) -> "Model":
        """
        Enable or disable parallel calls to multiple tools.

        Args:
            enable (bool): True to enable parallel tool calls, False to disable.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.parallel_tool_calls = enable
        return self

    def set_user(self, user: str) -> "Model":
        """
        Assign a unique user identifier, useful for tracking or analytics.

        Args:
            user (str): A string identifying the end-user.

        Returns:
            Model: The current Model instance (for fluent chaining).
        """
        self.user = user
        return self

    def build(self) -> "Model":
        """
        Finalize and return the fully configured Model object.

        This method can include validation or post-processing steps if needed.

        Returns:
            Model: The fully configured Model instance.
        """
        # Example validation (optional):
        # if self.stream and not self.stream_options:
        #     raise ValueError("Stream options must be set if streaming is enabled.")
        return self

    def __repr__(self) -> str:
        """
        Provide a concise string representation of the model configuration.

        Returns:
            str: A string summarizing key configuration parameters.
        """
        return (
            f"<Model developer={self.developer}, "
            f"modalities={self.modalities}, stream={self.stream}, ...>"
        )
