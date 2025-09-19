import pandas as pd
import os

data = {'Name':['Alice','Jhon','Bob'],
        'Age':[20,45,34],
        'city':['Kathmandu','Dhangadhi','Pokhara']}

df = pd.DataFrame(data)

#adding new row to df for v2
new_row_loc = {'Name': 'Gf1','Age':20,'city':'Chitwan'}
df.loc[len(df.index)] = new_row_loc

#Adding new row to df for v3
new_row_loc2 = {'Name':'Gf2','Age':22,'city':'Nepalgunj'}
df.loc[len(df.index)] = new_row_loc2


data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f'CSV file saved to {file_path}')
