import sqlite3

DATABASE = "fighters.db"
db = sqlite3.connect("DATABASE")
cursor = db.cursor()
sql = "SELECT * FROM fighters;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
