import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

print(type(data))

#load data into a DataFrame object:
df = pd.DataFrame(data)

# #return first row 
# print(df.loc[0])

# #Return row 0 and 1:
# print(df.loc[[0, 1]])

#df_clients = pd.read_csv("./Databases/Clients.csv")

df.to_csv('Databases/out.csv', index=False)
#FIX THIS ---> df.to_excel('Databases/out.xlsx',index=False)

# print(df_clients)