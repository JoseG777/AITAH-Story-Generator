from utils.logger import setup_logger

logger = setup_logger(__name__)


def handle_error(error):
    """Log an error and print a user-friendly message."""
    logger.error("An error occurred: %s", error)
    print(f"An error occurred: {error}")
