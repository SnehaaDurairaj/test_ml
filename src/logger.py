import logging
import os
from datetime import datetime


LOG_FILES = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILES)
os.makedirs(log_path, exist_ok=True)


LOG_FILES_PATH = os.path.join(log_path,LOG_FILES)

logging.basicConfig(
    
    filename=LOG_FILES_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, 
    
)



if __name__ == "__main__":
    logging.info("logging has started")