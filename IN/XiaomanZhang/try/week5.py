import requests
import pandas as pd

url = 'http://jsonplaceholder.typicode.com/users'
res = requests.get(url)
all_users = res.json()
#flatten
df = pd.json_normalize(all_users)

df = df[['username','email','address.zipcode','address.geo.lat','address.geo.lng','company.name']]
df.rename(columns={'address.zipcode':'zipcode','address.geo.lat':'lat', 'address.geo.lng':'lng','company.name':'company_name'}, inplace=True)

print(df)
#change dtype from object to float
df['lng'] = df['lng'].astype(str).astype(float)
df['lat'] = df['lat'].astype(str).astype(float)

df = df[df['lng'] > 0]
df_a = df[df['lat'] < 0]

print(df_a)
#write df_a into csv file
df_a.to_csv('output.csv')


