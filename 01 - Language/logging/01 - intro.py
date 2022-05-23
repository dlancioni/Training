import os
os.system("cls")
import logging


# Five log levels
# 1) debug    -> obvious
# 2) info     -> general information, MAYBE not important (17 users, new mails comming, etc)
# 3) warning  -> nothing critical, but something to pay attetion (disk space is 70%)
# 4) error    -> classic exception, something wrong but didn't crash yet
# 5) critical -> server down, crahs, etc

# security level defines the start level to use logs
# debug is level 1 shows all
# info is level 2 shows all except debugging
# warning is level 3 shows all except debugging, info
logging.basicConfig(level = logging.DEBUG)
logging.debug("Debugging...")
logging.info("Info...")
logging.warning("Warning...")
logging.critical("Critical...")