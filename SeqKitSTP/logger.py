# logger.py
"""
LOGGER SETUP FOR SeqKitSTP (DICTCONFIG VERSION)

----------------------------------------
WHAT THIS FILE DOES
----------------------------------------
This file sets up logging for the whole project.

We load configuration from settings.py and apply it.

----------------------------------------
HOW TO USE
----------------------------------------
Import this file ONCE at the start of your program:

    from SeqKitSTP import logger

After that, all files can use logging.

----------------------------------------
SIMPLE IDEA
----------------------------------------
settings.py → defines logging
logger.py   → turns logging ON
your files  → use logging

----------------------------------------
IMPORTANT
----------------------------------------
✔ Do NOT create loggers here
✔ Do NOT define handlers here
✔ Only apply configuration
"""

import logging.config

from SeqKitSTP.settings import LOGGING_CONFIG

# Apply logging configuration
logging.config.dictConfig(LOGGING_CONFIG)
