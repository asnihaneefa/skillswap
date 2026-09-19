import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
INSERT INTO students
(username, password_hash, full_name, email, phone, college, skills_teach, skills_learn)
VALUES
('testuser', 'test_password', 'Test Student', 'test@example.com', '9999999999', 'Test College', 'Python', 'UI UX')
""")

connection.commit()
connection.close()

print("Student added successfully!")