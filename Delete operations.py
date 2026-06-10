import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM employee WHERE id=?",
    (1,)
)

conn.commit()
conn.close()

print("Deleted Successfully")
