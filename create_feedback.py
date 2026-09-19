import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS feedback (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          student TEXT NOT NULL,
          teacher TEXT NOT NULL,
          skill TEXT NOT NULL,
          rating INTEGER,
          comment TEXT
)
""")

connection.commit()
connection.close()

print("Feedback table created successfully!")
