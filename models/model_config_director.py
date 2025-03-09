"""
ford begin_TODO
- Consider renaming the imported class "Config" to "ModelConfig" for better clarity.
- Consider renaming "ConfigDirector" to "ModelConfigDirector" to reflect its role.
- Update the return type annotations and docstrings in setter methods accordingly if renaming.
- Ensure consistency in naming conventions across modules (e.g., "Config" vs "ModelConfig").
end_todo

This module defines a Director class for constructing preset ModelConfig
instances. The Director orchestrates the configuration steps needed for
standard or specialized configurations.
"""

from typing import Any
from models import Config

class ConfigDirector:
    """
    The Director in the Builder pattern. Responsible for creating
    preset configurations for Config.
    """

    @staticmethod
    def default_config() -> Config:
        """
        Build and return a ModelConfig instance with default values.

        :return: A ModelConfig instance using its own defaults.
        """
        # If you want to override any defaults, chain the setter methods here.
        # For now, this simply returns a freshly built config as-is.
        return Config().build()


    @staticmethod
    def reliable_config() -> Config:
        """
        Build and return a ModelConfig instance with reliable settings.

        :return: A ModelConfig instance with preset parameters for reliable operation.
        """
        # If you want to override any defaults, chain the setter methods here.
        # For now, this simply returns a freshly built config as-is.
        return Config().set_max_completion_tokens(16384) \
                       .set_reasoning_effort("high") \
                       .set_max_completion_tokens(16384) \
                       .build() 

    @staticmethod
    def extensive_config() -> Config:
        """
        Build and return a ModelConfig instance with extensive settings.

        :return: A ModelConfig instance with additional parameters for extensive use cases.
        """
        # If you want to override any defaults, chain the setter methods here.
        # For now, this simply returns a freshly built config as-is.
        return Config().set_max_completion_tokens(16384) \
                       .set_reasoning_effort("high") \
                       .set_presence_penalty(1.35) \
                       .set_max_completion_tokens(16384) \
                       .build() 


    @staticmethod
    def creative_config() -> Config:
        """
        Build and return a ModelConfig instance with creative settings.

        :return: A ModelConfig instance configured for creative applications.
        """
        # If you want to override any defaults, chain the setter methods here.
        # For now, this simply returns a freshly built config as-is.
        return Config().set_max_completion_tokens(16384) \
                       .set_reasoning_effort("high") \
                       .set_presence_penalty(1.7) \
                       .set_max_completion_tokens(16384) \
                       .set_temperature(1.4) \
                       .build()
