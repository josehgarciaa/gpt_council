"""
ford begin_TODO
- Rename 'correct_login' to 'is_authenticated' to clearly indicate it is a boolean flag.
- Consider renaming 'client' to 'openai_client' for better specificity.
- Optionally, rename 'login' to 'authenticate' to better convey its purpose.
- Ensure that print statements in production code are replaced by proper logging.
end_todo

Module: Authentication Service
This module provides an authentication service specialized for OpenAI.
It retrieves API keys from environment variables (via a .env file) or directly via parameters,
and returns a fully authenticated OpenAI client.
"""

from authentication import SessionManager
from typing import Optional
from openai import OpenAI


class AuthenticationService:
    """
    AuthenticationService provides functionality to authenticate and manage a session for OpenAI.

    This class leverages a SessionManager to handle API key management. It can accept an API key directly,
    or load it from a .env file if none is provided. Upon successful validation of the API key,
    an OpenAI client is created and stored for further operations.

    Attributes:
        session_manager (SessionManager): Manages the API key, including setting, loading, and clearing it.
        client (Optional[OpenAI]): Holds the authenticated OpenAI client once login is successful.
        correct_login (bool): Flag indicating whether authentication was successful.

    Methods:
        login(api_key: Optional[str]): Authenticates by setting the API key and initializing the OpenAI client.
        get_client(): Returns the authenticated OpenAI client if login was successful.
        logout(): Logs out by clearing the session.
        is_logged_in(): Checks if the current session is authenticated.
    """

    def __init__(self):
        """
        Initialize the AuthenticationService instance.

        Initializes the SessionManager, and sets up the client and authentication flag.
        """
        self.session_manager = SessionManager()
        self.client = None
        self.correct_login = False

    def login(self, api_key: Optional[str] = None):
        """
        Authenticate the user and create an OpenAI client.

        If an API key is provided, it is set in the session manager.
        Otherwise, the API key is loaded from a .env file.
        The method validates the API key format via the session manager and, upon success,
        creates and stores an OpenAI client.

        Args:
            api_key (Optional[str]): The API key to authenticate with. If None, the API key will be loaded from the .env file.

        Raises:
            ValueError: If the API key format is invalid (i.e., authentication fails).
        """
        if api_key is not None:
            self.session_manager.set_api_key(api_key)
        else:
            self.session_manager.load_dotenv()

        if not self.session_manager.is_authenticated:
            raise ValueError("Authentication failed: Invalid API key format")
        print("Authentication successful.")

        if self.client is None:
            self.client = OpenAI(api_key=self.session_manager.api_key)
        self.correct_login = True

    def get_client(self):
        """
        Retrieve the authenticated OpenAI client.

        Returns:
            OpenAI: The authenticated OpenAI client if the login was successful.
            None: If the authentication has not been performed or failed.
        """
        if self.correct_login:
            return self.client
        else:
            print("The Authenticator was not able to login or it was not logged")
            return None

    def logout(self):
        """
        Log out the user by clearing the session and resetting the authentication flag.

        This method clears the stored API key and client information, effectively logging out the user.
        """
        self.session_manager.clear_session()
        self.correct_login = False
        print("Logout successful.")

    def is_logged_in(self):
        """
        Check if the user is currently authenticated.

        Returns:
            bool: True if the session is authenticated, False otherwise.
        """
        return self.session_manager.is_authenticated
