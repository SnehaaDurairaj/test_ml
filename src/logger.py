import logging
import os
from datetime import datetime
 
# Here we are creating a log file name that includes the current date and time.
# We are using the current date and time to ensure that each log file is unique.
# We are also storing the log files in a subdirectory called 'logs'.

LOG_FILES = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILES)
os.makedirs(log_path, exist_ok=True)
 
# The path to the log file.
LOG_FILES_PATH = os.path.join(log_path, LOG_FILES)
 
# Here we are configuring the logging module to log messages to a file.
# The filename parameter specifies the path to the log file.
# The format parameter specifies the format of each log message.
# The level parameter specifies the minimum severity level of log messages to be logged.
LOG_FILES_PATH = os.path.join(log_path,LOG_FILES)

logging.basicConfig(
    
     filename=LOG_FILES_PATH,
     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
     level=logging.INFO, 
    
)
 
# If the script is run as the main module, we are logging a message to indicate that logging has started.
if __name__ == "__main__":
     logging.info("logging has started")