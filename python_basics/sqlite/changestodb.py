import sqlite3

conn = sqlite3.connect("app.db")
conn.execute("pragma foreign_keys = ON;")
cursor = conn.cursor()

cursor.execute("update users set role = ? where id =?", ('Admin', 8))
conn.commit()
conn.close()
print("Table Update")



