# this constructor is for logging
'''this code configures the logging behavior for the package by setting the desired log format, directing log messages
 to a file and the console, and creating a logger object to be used in the package's modules'''

import os
import sys
import logging

logging_str = "[%(asctime)s:%(levelname)s: %(module)s:%(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), #Adds a handler that directs log messages to the specified log file.
        logging.StreamHandler(sys.stdout) # Adds a handler that directs log messages to the std o/p(console) for printing.
    ]
)

logger = logging.getLogger("cnnClassifierLogger")