import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
INSERT INTO students
(username, password_hash, full_name, email, phone, college, skills_teach, skills_learn)
VALUES
('testuser2', 'test_password2', 'Second Student', 'test2@example.com', '8888888888', 'Test College', 'UI UX', 'Python')
""")

connection.commit()
connection.close()

print("Second student added successfully!")