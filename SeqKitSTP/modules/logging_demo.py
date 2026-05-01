# modules/logging_demo.py
"""
LOGGING DEMONSTRATION SCRIPT

----------------------------------------
WHAT THIS SCRIPT DOES
----------------------------------------
This script demonstrates how to use logging properly
by retrieving a logger and using different log levels.

----------------------------------------
IMPORTANT CONCEPT
----------------------------------------
Logging is configured centrally at the top level of
the package (in SeqKitSTP.logger).

In this module (e.g. SeqKitSTP.modules.*), we DO NOT
create or configure logging again.

Instead, we retrieve a module-specific logger using:

    logging.getLogger(__name__)

✔ Python automatically assigns a name based on the
  module path (e.g. SeqKitSTP.modules.logging_demo)

✔ This logger is part of the hierarchy rooted at
  the top-level SeqKitSTP configuration

✔ Because logging was already initialised at import:
    from SeqKitSTP import logger

  → all modules automatically inherit:
    - log level
    - handlers
    - formatting

✔ Unless a logger is explicitly defined in settings.py,
  this module logger simply inherits behaviour from
  the ROOT logger

----------------------------------------
KEY DESIGN PRINCIPLE
----------------------------------------

✔ Configure logging ONCE at the top-level package
✔ Use logging everywhere via getLogger(__name__)
✔ Let inheritance handle consistency

----------------------------------------
FRAMEWORK / WEB APP NOTE
----------------------------------------

✔ In larger applications (e.g. web apps):
  - The parent application may override logging
  - Your module-level loggers will integrate naturally

✔ This works because:
  - logger names follow the package hierarchy
  - configuration is centralised and inheritable

----------------------------------------
LOGGING LEVELS DEMONSTRATED
----------------------------------------
DEBUG    → Detailed technical information (for developers)
INFO     → Normal program operation messages
WARNING  → Something unexpected, but program continues
ERROR    → Something failed during execution
CRITICAL → Serious failure, program may stop
"""

# Step 2: Get the logger (this is the key idea)
import logging
logger = logging.getLogger(__name__)


def logging_demo():
    # --------------------------------------------------
    # DEMO: Different logging levels
    # --------------------------------------------------

    logger.debug("DEBUG: Detailed info for debugging problems.")

    logger.info("INFO: The program has started successfully.")

    logger.warning("WARNING: Something unexpected happened, but continuing.")

    logger.error("ERROR: Something failed during execution.")

    logger.critical("CRITICAL: Serious failure - program may stop.")


    # --------------------------------------------------
    # FINAL MESSAGE
    # --------------------------------------------------

    logger.info("Demo complete. Check the console and log file.")

    return None

if __name__ == '__main__':
    logging_demo()

