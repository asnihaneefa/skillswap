from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Flask is running perfectly on my PC!"

@app.route("/students")
def students():
    return "Students page is working!"

@app.route("/matches")
def matches():
    import sqlite3

    connection = sqlite3.connect("students.db")

    students = connection.execute("""
    SELECT full_name, skills_teach, skills_learn
    FROM students
    """).fetchall()

    matches = []

    for student1 in students:
        for student2 in students:
            if student1 != student2:
               if student1[2].lower() == student2[1].lower():
                  matches.append(
                      student1[0] + " can learn " +
                      student1[2] + " from " +
                      student2[0]
                      )

    connection.close()

    return "<br>".join(matches)


@app.route("/sessions")
def sessions():
    import sqlite3

    connection = sqlite3.connect("students.db")

    session_list = connection.execute("""
    SELECT learner, teacher, skill, status
    FROM sessions
    """).fetchall()

    connection.close()

    result = []

    for session in session_list:
        result.append(
            session[0] + " requested to learn " +
            session[2] + " from " +
            session[1] + " - " +
            session[3]
        )

    return "<br>".join(result)



@app.route("/api/matches")
def api_matches():
    import sqlite3

    connection = sqlite3.connect("students.db")

    students = connection.execute("""
    SELECT full_name, skills_teach, skills_learn
    FROM students
    """).fetchall()

    connection.close()

    matches = []

    for student1 in students:
        for student2 in students:
            if student1 != student2:
               if student1[2].lower() == student2[1].lower():
                  matches.append({
                      "learner": student1[0],
                      "skill": student1[2],
                      "teacher": student2[0]
                  })

    return matches





