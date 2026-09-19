import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password_hash TEXT NOT NULL,
full_name TEXT NOT NULL,
email TEXT NOT NULL,
phone TEXT,
college TEXT,
skills_teach TEXT,
skills_learn TEXT
)
""")

connection.commit()
connection.close()

print("Database created successfully!")