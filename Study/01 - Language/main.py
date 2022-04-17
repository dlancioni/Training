"""
do somethibng magic
"""
import os
from datetime import datetime
os.system("cls")

import pandas as pd
df = pd.DataFrame({'Quantidade':[200, 350, 550], 'Taxa (%)':[20, 8, 15]})
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(df)





def xurrent_time():
    """
    abcde
    """
    now = datetime.now()
    return now.strftime("%H:%M:%S")
