import logging

# Create a custom filter
class MyFilter(logging.Filter):
    def filter(self, record):
        return 'important' in record.msg.lower()

# Set up the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the filter to the handler
handler.addFilter(MyFilter())

# Add the handler to the logger
logger.addHandler(handler)

# Now let's log some messages
logger.debug("This is a debug message")  # This won't be logged
logger.info("This is an important message")  # This will be logged
logger.warning("Another message")  # This won't be logged