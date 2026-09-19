import sqlite3

connection = sqlite3.connect("students.db")

students = connection.execute("SELECT * FROM students").fetchall()

for student in students:
    print(student)

connection.close()