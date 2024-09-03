import logging
# Basic configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Creating a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#
# # Logging messages
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")

def divide(x, y):
    logger.debug(f"Dividing {x} by {y}")
    if y == 0:
        logger.error("Attempted to divide by zero!")
        return None
    return x / y

result = divide(10, 2)
logger.info(f"Division result: {result}")
result = divide(10, 0)
logger.warning("Division operation failed")