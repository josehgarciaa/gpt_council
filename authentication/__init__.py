"""
ford begin_TODO
- Ensure consistency in naming conventions across all modules in the package.
- Optionally, include a changelog or author info for future reference.
end_todo

Module: authentication
This module aggregates the core components for managing API key sessions and authentication.
It exposes the SessionManager for handling API key retrieval and validation, and the
AuthenticationService for authenticating users and obtaining a fully initialized client.
This setup ensures flexibility and clarity in how the authentication processes are configured
and accessed across the package.
"""

__version__ = "1.0.0"

from .session_manager import SessionManager
from .auth_service import AuthenticationService
