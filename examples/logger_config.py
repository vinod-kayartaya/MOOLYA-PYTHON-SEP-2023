import logging


# logging.basicConfig(
#     level=logging.WARN,
#     format='%(asctime)s - %(levelname)s - %(name)s %(module)s %(message)s',
#     filename='app.log'
# )
#
# logger = logging.getLogger(__name__)

import logging

# Configure the root logger
logging.basicConfig(level=logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the root logger
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

