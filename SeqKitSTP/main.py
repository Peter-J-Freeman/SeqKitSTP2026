# main.py
"""
MAIN ENTRY POINT FOR SeqKitSTP

----------------------------------------
PURPOSE
----------------------------------------
This script acts as the application entry point.

It ensures:
✔ Logging is initialised once at startup
✔ Modules are then safely executed
✔ Logging behaviour is consistent across the application

----------------------------------------
STRUCTURE OVERVIEW
----------------------------------------

Step 1 → Initialise logging (EXPLICIT CALL)
Step 2 → Import/use application modules
Step 3 → Execute program logic

----------------------------------------
IMPORTANT DESIGN PRINCIPLE
----------------------------------------

✔ Logging MUST be configured once, at the start of main()

Why?

- logging.config.dictConfig(...) overwrites configuration
- Calling it multiple times can:
  → reset handlers
  → duplicate outputs
  → create inconsistent logging behaviour

Therefore:
✔ Call setup_logging() ONCE at the beginning
✔ Do NOT call it in multiple modules

----------------------------------------
HOW LOGGING WORKS AFTER SETUP
----------------------------------------

✔ After setup_logging() runs:

- All modules use:
      logging.getLogger(__name__)

- Python creates loggers based on module paths:
      SeqKitSTP.modules.logging_demo

- These loggers then:
  → inherit configuration from the ROOT logger
  → use the same handlers, levels, and formatters

✔ This means:
- We DO NOT pass logger objects around
- We DO NOT configure logging in modules

✔ Instead:
- We rely entirely on:
      getLogger(__name__)
  + central configuration

----------------------------------------
TEACHING TAKEAWAY
----------------------------------------

✔ Configure once → at application start
✔ Never reconfigure → prevents overwriting
✔ Use __name__ everywhere → automatic hierarchy

→ Simple, safe, and scalable logging
"""

# --------------------------------------------------
# STEP 1: Import logging setup function
# --------------------------------------------------
# No side effects — this only imports the function

from SeqKitSTP.logger import setup_logging


# --------------------------------------------------
# STEP 2: Import application modules
# --------------------------------------------------
# These modules will create loggers using __name__,
# but they will only behave correctly AFTER setup_logging()

from SeqKitSTP.modules import logging_demo


# --------------------------------------------------
# STEP 3: Main execution function
# --------------------------------------------------
def main():
    """
    Main application entry point.

    Responsibilities:
    ✔ Initialise logging ONCE
    ✔ Run application logic

    IMPORTANT:
    setup_logging() MUST be called before any logging is used
    """

    # Initialise logging (CRITICAL STEP)
    setup_logging()

    # Run demo module
    logging_demo.logging_demo()


# --------------------------------------------------
# ENTRY POINT GUARD
# --------------------------------------------------
# Ensures this script only runs when executed directly

if __name__ == "__main__":
    main()
