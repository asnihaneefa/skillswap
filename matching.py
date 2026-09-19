import sqlite3

connection = sqlite3.connect("students.db")

students = connection.execute("""
SELECT full_name, skills_teach, skills_learn
FROM students
""").fetchall()

for student1 in students:
    for student2 in students:
        if student1 != student2:
           if student1[2].lower() == student2[1].lower():
              print(student1[0], "can learn", student1[2], "from", student2[0])

connection.close()
