import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
INSERT INTO feedback (student, teacher, skill, rating, comment)
VALUES ('Test Student', 'Second Student', 'UI UX', 5, 'Very helpful session!')
""")

connection.commit()
connection.close()

print("Feedback added successfully!")
