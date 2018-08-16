import sqlite3
import pandas as pd

def getinput():
    dbname = input("Enter database name ")
    tablename = input("Enter table name ")
    #print(dbname+tablename)
    one(dbname,tablename)    
    
def one(dbname, tablename):
    conn = sqlite3.connect(dbname)
    print("Opened database successfully")
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * from COMPANY")
    rows = cursor.fetchall()
    print(rows)
    df = pd.read_sql_query("SELECT * FROM COMPANY", conn)
    print(df)
    conn.close()

def main():
    getinput()
if __name__ == "__main__":
    main()