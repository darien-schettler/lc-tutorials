"""This module contains the utility functions that help us run the tutorials."""

# Core Library modules
from lc_tutorials.appearance.notebook import cprint

# Third party imports
from dotenv import load_dotenv, find_dotenv


def setup_environment(verbose=True):
    """Set up the environment variables and initialize core components.

    Returns:
        bool: True if environment variables were loaded successfully
    """
    if load_dotenv(find_dotenv()):
        cprint("\n✅ Environment Variables Loaded Successfully\n", fg_color="green", bold=True)
    else:
        cprint("\n❌ Environment Variables Failed to Load\n", fg_color="red", bold=True)


