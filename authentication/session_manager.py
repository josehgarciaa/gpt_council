"""
ford begin_TODO
- Rename __instance to _instance to follow the common convention for internal variables.
- Consider adding a note in the class docstring that this is a Singleton implementation.
- Document the __new__ method to explain its role in the singleton pattern.
- Use logging instead of print statements (if applicable in the context) for better production practices.
end_todo

Module: Session Manager
This module provides the SessionManager class which is responsible for reading,
validating, and processing an API key before authenticating with the server.
The SessionManager is implemented as a singleton to ensure a single shared session state.
"""

import os
from dotenv import load_dotenv


class SessionManager:
    """
    SessionManager handles the retrieval and validation of an API key for authentication.

    This class reads the API key from a provided value or from a .env file,
    validates its format, and manages the session state (authenticated or not).
    It is implemented as a singleton, ensuring that only one instance exists
    during the application's lifecycle.

    Attributes:
        api_key (str or None): The API key used for authentication.
        is_authenticated (bool): Indicates whether the API key is valid.
    """

    __instance = None  # Consider renaming to _instance for internal convention

    def __new__(cls):
        """
        Create and return a singleton instance of SessionManager.

        If an instance already exists, this method returns it;
        otherwise, it creates a new instance and initializes the attributes.
        """
        if SessionManager.__instance is None:
            SessionManager.__instance = object.__new__(cls)
            SessionManager.__instance.api_key = None
            SessionManager.__instance.is_authenticated = False
        return SessionManager.__instance

    def set_api_key(self, api_key: str):
        """
        Set the API key and update the authentication status.

        Args:
            api_key (str): The API key to be set and validated.
        """
        self.api_key = api_key
        self.is_authenticated = self.validate_api_key(api_key)

    def load_dotenv(self) -> None:
        """
        Load the API key from a .env file and update the authentication status.

        This method loads environment variables from the .env file,
        retrieves the API key using the key "API_KEY", and validates it.
        """
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.is_authenticated = self.validate_api_key(self.api_key)

    def validate_api_key(self, api_key: str) -> bool:
        """
        Validate the format of the provided API key.

        This method checks if the API key starts with the expected prefix ("sk-")
        and meets a minimum length requirement.

        Args:
            api_key (str): The API key to validate.

        Returns:
            bool: True if the API key is valid, False otherwise.
        """
        # Add actual validation logic, possibly checking on OpenAI's side.
        # For demonstration, we check basic provisions:
        return api_key.startswith("sk-") and len(api_key) > 20

    def clear_session(self):
        """
        Clear the current session by resetting the API key and authentication status.

        This method sets the API key to None and marks the session as not authenticated.
        """
        self.api_key = None
        self.is_authenticated = False
