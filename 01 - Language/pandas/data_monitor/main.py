# https://pandas.pydata.org/docs/user_guide/merging.html

import os
import sys
import warnings
import numpy as np
import pandas as pd
warnings.simplefilter(action="ignore", category=FutureWarning)

BASE_FOLDER = "PS RiskDB Data Monitor"
BASE_PATH = "c:\\lancid\\data\\"
STATUS = "On"

def get_base(level):
    data = {"Level" :[level, level, level, level, level],"BusinessLine" :["CLEARING","DCS", "FUTURES", "PB", "SPG"]}
    cols = ["Level","BusinessLine"]
    df = pd.DataFrame(data, columns=cols)
    return df

def get_empty(level):
    level = f"Level {level}"
    data = {"BusinessLine" :["CLEARING","DCS", "FUTURES", "PB", "SPG"], level :[0, 0, 0, 0, 0]}
    cols = ["BusinessLine", level]
    df = pd.DataFrame(data, columns=cols)
    return df

def trim_all_columns(df):
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)

def get_timed(level, dt, tm):   
    file_name = f"{BASE_FOLDER} {dt} {tm}.csv"
    path = f"{BASE_PATH}{BASE_FOLDER} {dt}\\{file_name}"
    df1 = pd.read_csv(path, ",")    
    df1 = trim_all_columns(df1)    
    col_bl = "BusinessLine"
    col_lv = f"Level {level}"   
    df1 = df1[[col_bl, col_lv]]
    df1 = df1[df1[col_lv] == STATUS]
    df1 = df1.groupby([col_bl])[col_lv].count().reset_index()    
    df2 = get_empty(level)
    df = df1.set_index(col_bl).combine_first(df2.set_index(col_bl)).reset_index()
    df.rename(columns={col_lv:tm}, inplace=True)    
    return df

def main(dt, tms):
    result = []
    for level in [1,2,3,4]:
        df1 = get_base(level)
        for tm in tms:
            df2 = get_timed(level, dt, tm)
            df1 = pd.merge(df1, df2, on="BusinessLine")
        result.append(df1)
    result = pd.concat(result)
    return result


dt = sys.argv[1]
tms = []
path = f"{BASE_PATH}{BASE_FOLDER} {dt}"
files = os.listdir(path)
os.system("cls")
print("Processing date ", dt)
if len(files) == 0:
    print("No file at ", path)
else:
    print("Processing ", len(files), " files")
    for file in files:
        if (file[32:36] != ""):
            tms.append(file[32:36])
    tms.sort()
    result = main(dt,tms)
    print(result)
    print("Results at ", path + "\\result.csv")
    result.to_csv(path + "\\result.csv")


