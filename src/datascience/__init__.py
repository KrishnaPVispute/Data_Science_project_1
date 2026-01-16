import logging
import os
import sys

logging_str='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s]'

log_dir ='logs'
log_filepath = os.path.join(log_dir,'logging.log')
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
level=logging.INFO,format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),#
        logging.StreamHandler(sys.stdout)#If we run code in terminal we able to see the message store inside the file
    ]
)
logging = logging.getLogger('d atasciencelogger')