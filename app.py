from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

# Create tables
def init_db():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS competition (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        competition_id INTEGER,
        student_name TEXT,
        project_title TEXT,
        score INTEGER DEFAULT 0
    )
    """)

    db.commit()
    db.close()

init_db()

@app.route("/")
def index():
    db = get_db()
    competitions = db.execute("SELECT * FROM competition").fetchall()
    return render_template("index.html", competitions=competitions)

@app.route("/create", methods=["GET", "POST"])
def create_competition():
    if request.method == "POST":
        name = request.form["name"]
        db = get_db()
        db.execute("INSERT INTO competition (name) VALUES (?)", (name,))
        db.commit()
        return redirect("/")
    return render_template("create_competition.html")

@app.route("/submit/<int:cid>", methods=["GET", "POST"])
def submit_project(cid):
    if request.method == "POST":
        student = request.form["student"]
        title = request.form["title"]

        db = get_db()
        db.execute("""
        INSERT INTO project (competition_id, student_name, project_title)
        VALUES (?, ?, ?)
        """, (cid, student, title))
        db.commit()
        return redirect("/")

    return render_template("submit_project.html")

@app.route("/judge/<int:cid>", methods=["GET", "POST"])
def judge(cid):
    db = get_db()

    if request.method == "POST":
        pid = request.form["pid"]
        score = request.form["score"]
        db.execute("UPDATE project SET score=? WHERE id=?", (score, pid))
        db.commit()

    projects = db.execute(
        "SELECT * FROM project WHERE competition_id=?", (cid,)
    ).fetchall()

    return render_template("judge.html", projects=projects)

@app.route("/leaderboard/<int:cid>")
def leaderboard(cid):
    db = get_db()
    projects = db.execute("""
    SELECT student_name, project_title, score
    FROM project
    WHERE competition_id=?
    ORDER BY score DESC
    """, (cid,)).fetchall()

    return render_template("leaderboard.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
