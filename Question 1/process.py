import numpy as np
import pandas as pd

#read both csv into dataframes
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')

#merge the dataframes together
df3 = pd.concat([df1, df2], ignore_index=True)

#first filter the rows without names
df3 = df3[df3.name.notnull()]

#spilt the column name into first_name and last_name based on space 
df3[['first_name', 'last_name']] = df3['name'].str.split(' ', 1, expand=True)

#set price as float, this gets rid of the extra 0's as well
df3['price'] = df3['price'].astype(float)

#create column above_100, true if price above 100, false if price below 100
df3['above_100'] = df3['price'].apply(lambda x: True if x > 100 else False) 

#reorder the colums, dropping name in the process
df3 = df3[['first_name', 'last_name', 'price', 'above_100']]

#output to csv file
df3.to_csv('processed.csv', index=False, header = True) 