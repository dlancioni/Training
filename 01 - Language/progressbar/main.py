# https://pypi.org/project/progress/

import os
from progress.bar import ShadyBar
from progress.bar import Bar

os.system("cls")
total = 10
#bar = ShadyBar('Running recon', max=total)
bar = Bar('Running recon', max=total)
for i in range(total):   
    bar.next()
    print("total")
bar.finish()
