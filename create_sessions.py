import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    learner TEXT NOT NULL,
    teacher TEXT NOT NULL,
    skill TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
""")

connection.commit()
connection.close()

print("Sessions table created successfully!")