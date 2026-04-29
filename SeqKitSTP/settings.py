# settings.py
"""
LOGGING CONFIGURATION (DEFENSIVE VERSION)

----------------------------------------
WHAT THIS TEACHES
----------------------------------------
✔ Centralised logging configuration
✔ Safe file handling
✔ Defensive programming

KEY IDEA:
Even when things seem simple, we still validate inputs.
"""

import os

# --------------------------------------------------
# STEP 1: Define default log file (hidden, home directory)
# --------------------------------------------------
home_dir = os.path.expanduser("~")
DEFAULT_LOG = os.path.join(home_dir, ".seqkitstp.log")

# In this teaching example, we don't read config yet,
# but we structure this so it could be extended later
LOG_FILE = DEFAULT_LOG


# --------------------------------------------------
# STEP 2: NORMALISE the path (defensive step)
# --------------------------------------------------
# Handles "~", relative paths, etc.
LOG_FILE = os.path.abspath(os.path.expanduser(LOG_FILE))


# --------------------------------------------------
# STEP 3: Ensure directory exists
# --------------------------------------------------
log_dir = os.path.dirname(LOG_FILE)
if log_dir:
    os.makedirs(log_dir, exist_ok=True)


# --------------------------------------------------
# STEP 4: Logging configuration
# --------------------------------------------------
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "standard": {
            "format": (
                "%(asctime)s | %(levelname)s | %(name)s | "
                "%(filename)s:%(lineno)d | %(message)s"
            )
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": LOG_FILE,
        },
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    }
}
