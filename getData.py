import os
import json
import gzip
import pandas as pd
from urllib.request import urlopen

#for meta data = product info etc
meta_data = []
with gzip.open('meta_Computers.json.gz') as f: #obviously change the file name
    for l in f:
        meta_data.append(json.loads(l.strip()))
    
# total length of list, this number equals total number of products
print(len(meta_data))

# first row of the list
print(meta_data[0])

df = pd.DataFrame.from_dict(meta_data)

print(len(df))

df3 = df.fillna('')
df4 = df3[df3.title.str.contains('getTime')] # unformatted rows
df5 = df3[~df3.title.str.contains('getTime')] # filter those unformatted rows
print(len(df4))
print(len(df5))

#for review data
review_data = []
with gzip.open('meta_Computers.json.gz') as f: #obviously change the file name
    for l in f:
        review_data.append(json.loads(l.strip()))
    
# total length of list, this number equals total number of products
print(len(review_data))

# first row of the list
print(review_data[0])

df = pd.DataFrame.from_dict(review_data)

print(len(df))

df3 = df.fillna('')
df4 = df3[df3.title.str.contains('getTime')] # unformatted rows
df5 = df3[~df3.title.str.contains('getTime')] # filter those unformatted rows
print(len(df4))
print(len(df5))



