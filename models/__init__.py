"""
ford begin_TODO
- Consider renaming "Config" to "ModelConfig" for better clarity and consistency.
- Consider renaming "ConfigAdapter" to "ModelConfigAdapter" to clearly indicate its purpose.
- Consider renaming "ConfigDirector" to "ModelConfigDirector" for consistency with naming conventions.
- Consider renaming "Director" to "ModelDirector" to reflect its role in model construction.
end_todo

Module: models
Version: 1.0.0

This package provides the core components for model configuration and construction.
It aggregates the following modules:
    - model_config (Config): A builder-style class for configuring chat completion
      parameters.
    - model (Model): Defines the model configuration and behavior.
    - model_config_adapter (ConfigAdapter): Specializes a generic configuration to
      the specific requirements of a given model type.
    - model_config_director (ConfigDirector): Provides preset configurations for models.
    - model_director (Director): Orchestrates the creation of different types of models
      using the builder pattern.
"""

from .model_config import Config
from .model import Model
from .model_config_adapter import ConfigAdapter
from .model_config_director import ConfigDirector
from .model_director import Director
