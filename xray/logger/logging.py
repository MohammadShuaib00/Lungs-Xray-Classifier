import os
from datetime import datetime
import logging

# Generate a unique Log file name based on the current datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_H_%M_%S')}.log"

# Define the path to the 'logs' directory
LOG_PATH = os.path.join(os.getcwd(), "logs")

# Create the 'logs' directory if it does not exist
os.makedirs(LOG_PATH, exist_ok=True)

# Join the file path to create the complete log file path
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

# Configuration for logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s - %(module)s - Line: %(lineno)d",
)


