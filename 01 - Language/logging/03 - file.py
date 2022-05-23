import os
os.system("cls")
import logging

logging.basicConfig(filename="./log.txt",
                    filemode="a",
                    format="[%(levelname)s] %(name)s %(asctime)s: %(message)s",
                    datefmt="%Y%m%d %H%M",
                    level=logging.DEBUG)
logger = logging.getLogger("LANCID")

for item in range(1, 10):
    logger.info("Logging line number {}".format(item))

