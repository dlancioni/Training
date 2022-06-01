import os
import subprocess


x = subprocess.run("dir", shell=True, capture_output=True);

x = os.system("dir")
