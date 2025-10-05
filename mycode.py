import pandas as pd
import os

data = {'Name': ['Alice', 'Bob', 'Charles'],
        'Age': [13, 20, 69],
        'City': ['NYC', 'Karachi', 'Islamabad']}

df = pd.DataFrame(data)

new_row_data = {'Name': 'BabyDoll', 'Age': '24', 'City': 'Lahore'}
df.loc[len(df.index)] = new_row_data

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f'cvf file saved to {file_path}')