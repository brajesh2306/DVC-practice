import pandas as pd
import os
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

new_row_lock = {'name':'brajesh','age':20,"city":'pipariya'}
df.loc[len(df.index)] = new_row_lock

new_row_lock2 = {'name':'apporv','age':28,"city":'assam'}
df.loc[len(df.index)] = new_row_lock

data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

file_path = os.path.join(data_dir, "sample_data.csv")
df.to_csv(file_path, index=False)    