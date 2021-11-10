import os
os.system("cls")
import logging

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger("LANCID")   # change root to lancid
logger.info(" Something to log")
logger.log(logging.INFO, " More information to log")