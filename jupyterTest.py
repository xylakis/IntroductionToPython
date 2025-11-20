#%%

import pandas as pd 
import numpy as np 
import psycopg2
# %%
conn = psycopg2.connect(host="localhost", dbname="analysis", user="postgres", password="Suxumuxu3003!",
                         port=5432)

cur = conn.cursor()
# %%
query = "SELECT * FROM teachers"

 # Load data into a Pandas DataFrame
df = pd.read_sql_query(query, conn)
# %%
conn.commit()
cur.close()
conn.close()
# %%
