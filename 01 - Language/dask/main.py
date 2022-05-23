import os
import dask.dataframe as dd


os.system("cls")
path = "c:\\temp\\bigfile.csv"
x = dd.read_csv(path, sample_rows=10)
print(x)