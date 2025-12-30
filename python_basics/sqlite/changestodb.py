import sqlite3

conn = sqlite3.connect("app.db")
conn.execute("pragma foreign_keys = ON;")
cursor = conn.cursor()

cursor.execute(" select * from users")

rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()

conn.close()

