"""
ford begin_TODO
- Rename class "Director" to "ModelDirector" for greater clarity in the context of model configuration.
- Update docstrings for each method to clearly differentiate the configurations provided.
- Verify consistency in terminology between "developer" and "administrator" in the documentation.
end_todo

Module: models.model_director
Description: This module defines a director class responsible for orchestrating the creation
of different Model configurations using the builder pattern. The director leverages the Model
class to provide preset configurations for default use, Python programming expertise, and creative writing.
"""

from models import Model


class Director:
    """
    Director class in the Builder pattern responsible for orchestrating
    the configuration of Model instances.

    This class provides static methods that build Model instances with preset configurations.
    """

    @staticmethod
    def default_model() -> Model:
        """
        Build and return a default-configured Model instance.

        The default configuration sets the model type to "gpt-4o-mini" and assigns a generic
        developer instruction that prompts the model to provide concise answers.

        Returns:
            Model: A fully built Model instance with default settings.
        """
        return (
            Model()
            .set_model_type("gpt-4o-mini")
            .set_developer_instruction("You are a generic assistant that tries to answer as concise as possible")
            .build()
        )

    @staticmethod
    def python_programmer() -> Model:
        """
        Build and return a Model instance configured for a Python programming expert.

        This configuration sets the model type to "o3-mini" and provides a detailed developer instruction
        for code review tasks. The instruction emphasizes a direct language, brevity, and a focus on
        consistency, documentation, PEP compliance, and common Python pitfalls.

        Returns:
            Model: A fully built Model instance configured for Python programming review.
        """
        return (
            Model()
            .set_model_type("o3-mini")
            .set_developer_instruction(
                "You are a python programming expert that is overviewing the software of the user. "
                "You should use a direct language with a short amount of words and provide information "
                "about lack of consistency, lack of documentation, problems with PEP compliance, and check "
                "for common pitfalls occurring when programming with Python. Readability and maintainability "
                "should be priorities."
            )
            .build()
        )

    @staticmethod
    def writer() -> Model:
        """
        Build and return a Model instance configured for creative writing tasks.

        This configuration sets the model type to "gpt-4o" and assigns a creative writer instruction.

        Returns:
            Model: A fully built Model instance configured for creative writing.
        """
        return (
            Model()
            .set_model_type("gpt-4o")
            .set_developer_instruction("You are a creative writer")
            .build()
        )
