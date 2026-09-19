import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
INSERT INTO sessions (learner, teacher, skill)
VALUES ('Test Student', 'Second Student', 'UI UX')
""")

connection.commit()
connection.close()

print("Session request added successfully!")
