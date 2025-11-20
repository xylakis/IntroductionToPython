import psycopg2
import pandas as pd

conn = psycopg2.connect(host="localhost", dbname="analysis", user="postgres",
                        password="Suxumuxu3003!", port=5432)

cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS students (
#             id INT PRIMARY KEY,
#             name VARCHAR(255),
#             age INT, 
#             gender CHAR
#             )""")

# cur.execute("""INSERT INTO students (id, name, age, gender) VALUES 
#             (1, 'Mike', 30, 'f'), 
#             (2, 'Mickey', 30, 'm'), 
#             (3, 'Claudia', 30, 'f'), 
#             (4, 'Mike', 30, 'f'), 
#             (5, 'Johnny', 30, 'm')

# """)

query = "SELECT * FROM teachers"

 # Load data into a Pandas DataFrame
df = pd.read_sql_query(query, conn)

conn.commit()

cur.close()
conn.close()

print(df)

