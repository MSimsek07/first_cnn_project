# LOGGING
# We could create a seperated folder for logging but
# to make import statement shorter and easy to access for all componenets, creating logging in this constructer file is much better,
# so we can import it from anywhere in the project like this "from cnnClassifier import logger" ,
# instead of importing like this "from src.cnnClassifier import logger"
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
