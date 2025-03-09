"""
ford begin_TODO
- Consider renaming the class "ConfigAdapter" to "ModelConfigAdapter" for clarity.
- In the adapt() method, consider renaming the parameter "model" to "model_instance" to avoid potential confusion.
- Update the adapt() docstring: change "model_type" to "model" since a Model instance is expected.
- Replace print statements with logging for production use.
end_todo

Implements a ModelConfigAdapter that specializes a generic Config
preset based on the provided model_type. This adapter can remove or adapt
parameters that don’t apply to a given model.
"""

import copy
from models import Config, Model

class ConfigAdapter:
    # Define restrictions or adjustments based on model type.
    # For example, which parameters are not applicable for a model.
    _restricted_params = {
        # For model type "o3-mini", remove these config keys.
        "gpt-4o-mini": ["reasoning_effort"],
        # For model type "gpt-4o-mini", remove or adjust these keys.
        "gpt-4o": ["reasoning_effort"],
        "gpt-4.5": ["reasoning_effort"],
        "o3-mini": ["frequency_penalty", "top_p", "presence_penalty", "temperature"],
        "o1": ["frequency_penalty", "top_p", "presence_penalty", "temperature"]
    }

    @staticmethod
    def adapt(config: Config, model: Model) -> Config:
        """
        Adapts the given configuration for the specified model.

        This method examines the model's model_type and removes, nullifies,
        or adjusts parameters in the configuration that are not applicable
        for that specific model type.

        Args:
            config (Config): A Config instance containing the preset parameters.
            model (Model): A Model instance whose model_type is used to determine
                           the necessary adaptations.

        Returns:
            Config: The adapted Config instance with modifications applied
                  according to the model's restrictions.
        """
        # Retrieve current parameters as a dict, if needed.
        sp_config = copy.copy(config)
        params = sp_config.get_params()

        # Get the list of keys to restrict for this model, if any.
        model_type = model.model_type
        print(model_type)
        keys_to_remove = ConfigAdapter._restricted_params.get(model_type, [])

        # Remove or adjust each restricted parameter.
        for key in keys_to_remove:
            if key in params:
                # Option A: Remove the parameter completely.
                # One way is to set the attribute to None.
                setattr(sp_config, key, None)
                # Alternatively, if you want to remove from the dictionary,
                # you could delete it from params—but note that
                # config.get_params() builds the dictionary dynamically.
                # So setting the underlying attribute to None is sufficient.
        # Further adaptation rules can go here:
        # For instance, if a parameter’s value is out of range for a model,
        # you might adjust it:
        if (model_type == "gpt-4o-mini") or (model_type == "gpt-4o"):
            sp_config.set_reasoning_effort(None)

        # At this point, you can either return the modified config
        # or even build a fresh dict if desired.
        return sp_config
