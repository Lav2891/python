import sqlite3
import pandas as pd

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully");

cursor = conn.cursor()
cursor = conn.execute("SELECT * from COMPANY")
rows = cursor.fetchall()
print(rows)
type(rows)
#df = pd.DataFrame(rows)
#print (df)
df = pd.read_sql_query("SELECT * FROM COMPANY", conn)
print(df)

for x in rows:
   print ("ID = ", rows[0])
   print ("NAME = ", rows[1])
   print ("ADDRESS = ", rows[2])
   print ("SALARY = ", rows[3], "\n")
   

conn.close()