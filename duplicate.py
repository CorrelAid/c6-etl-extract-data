import pandas as pd
import numpy as np
import csv

df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')
df3 = pd.read_csv('file3.csv')
df4 = pd.read_csv('file4.csv')

df_names_list = [df1, df2, df3, df4]

for x in df_names_list:
    x.drop_duplicates(keep='first', inplace=True)
    
    with open('results.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.close()