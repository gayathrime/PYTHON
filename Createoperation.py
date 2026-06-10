import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO employee(name, department) VALUES(?, ?)",
    ("Gayathri", "IT")
)

conn.commit()
conn.close()

print("Record Inserted")
