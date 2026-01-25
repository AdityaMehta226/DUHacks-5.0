from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3
import os
import io
import zipfile
import shutil
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "ddu_hacks_final_master" 

# Configuration for file storage and uploads
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['PROJECT_FOLDER'] = 'static/projects'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROJECT_FOLDER'], exist_ok=True)

def get_db():
    """Establishes connection to the SQLite database"""
    db = sqlite3.connect("database.db")
    db.row_factory = sqlite3.Row 
    return db

def init_db():
    """Initializes the database schema"""
    with get_db() as db:
        db.execute("CREATE TABLE IF NOT EXISTS competition (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
        db.execute("""CREATE TABLE IF NOT EXISTS project (
            id INTEGER PRIMARY KEY AUTOINCREMENT, competition_id INTEGER,
            student_name TEXT, project_title TEXT, score INTEGER DEFAULT 0,
            submission_type TEXT, submission_content TEXT)""")
        db.execute("""CREATE TABLE IF NOT EXISTS user_profile (
            id INTEGER PRIMARY KEY, username TEXT, post TEXT, image_path TEXT)""")
        
        # Default user setup for the team
        if not db.execute("SELECT * FROM user_profile").fetchone():
            db.execute("INSERT INTO user_profile (id, username, post, image_path) VALUES (1, 'Aditya Mehta', 'Developer', 'default.png')")
        db.commit()

init_db()

def get_user():
    """Fetches user data and generates initials (e.g., 'AM')"""
    db = get_db()
    user = db.execute("SELECT * FROM user_profile WHERE id=1").fetchone()
    user_dict = dict(user)
    names = user_dict['username'].split()
    initials = "".join([n[0].upper() for n in names[:2]]) if names else "U"
    user_dict['initials'] = initials
    return user_dict

@app.route("/")
def index():
    db = get_db()
    competitions = db.execute("SELECT * FROM competition").fetchall()
    return render_template("index.html", competitions=competitions, user=get_user())

@app.route("/settings", methods=["GET", "POST"])
def settings():
    """Profile management with safety checks to prevent KeyErrors"""
    db = get_db()
    if request.method == "POST":
        username = request.form.get("username")
        post = request.form.get("post")
        
        if username and post:
            file = request.files.get("profile_pic")
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                db.execute("UPDATE user_profile SET username=?, post=?, image_path=? WHERE id=1", (username, post, filename))
            else:
                db.execute("UPDATE user_profile SET username=?, post=? WHERE id=1", (username, post))
            db.commit()
        return redirect(url_for('settings'))
    return render_template("settings.html", user=get_user())

@app.route("/remove_pic", methods=["POST"])
def remove_pic():
    """Resets profile image to trigger initials fallback"""
    db = get_db()
    db.execute("UPDATE user_profile SET image_path='default.png' WHERE id=1")
    db.commit()
    return redirect(url_for('settings'))

@app.route("/about")
def about():
    """Credits page for Aditya, Vatsal, Hetvi, and Shrushti"""
    return render_template("about.html", user=get_user())

@app.route("/submit/<int:cid>", methods=["GET", "POST"])
def submit_project(cid):
    db = get_db()
    if request.method == "POST":
        student, title, sub_type = request.form["student"], request.form["title"], request.form["submission_type"]
        if sub_type == 'link':
            content = request.form["project_link"]
        else:
            files = request.files.getlist("project_folder")
            folder_name = f"cid{cid}_{secure_filename(student)}"
            dest = os.path.join(app.config['PROJECT_FOLDER'], folder_name)
            os.makedirs(dest, exist_ok=True)
            for f in files: 
                if f.filename: f.save(os.path.join(dest, secure_filename(f.filename)))
            content = folder_name
        db.execute("INSERT INTO project (competition_id, student_name, project_title, submission_type, submission_content) VALUES (?, ?, ?, ?, ?)", 
                   (cid, student, title, sub_type, content))
        db.commit()
        return redirect(url_for('index'))
    comp = db.execute("SELECT name FROM competition WHERE id=?", (cid,)).fetchone()
    return render_template("submit_project.html", cid=cid, comp_name=comp['name'], user=get_user())

@app.route("/judge/<int:cid>", methods=["GET", "POST"])
def judge(cid):
    db = get_db()
    if request.method == "POST":
        db.execute("UPDATE project SET score=? WHERE id=?", (request.form["score"], request.form["pid"]))
        db.commit()
    comp = db.execute("SELECT name FROM competition WHERE id=?", (cid,)).fetchone()
    projects = db.execute("SELECT * FROM project WHERE competition_id=?", (cid,)).fetchall()
    enhanced = []
    for p in projects:
        item = dict(p)
        if p['submission_type'] == 'folder':
            path = os.path.join(app.config['PROJECT_FOLDER'], p['submission_content'])
            item['files'] = os.listdir(path) if os.path.exists(path) else []
        enhanced.append(item)
    return render_template("judge.html", projects=enhanced, cid=cid, comp_name=comp['name'], user=get_user())

@app.route("/leaderboard/<int:cid>")
def leaderboard(cid):
    db = get_db()
    comp = db.execute("SELECT name FROM competition WHERE id=?", (cid,)).fetchone()
    projects = db.execute("SELECT * FROM project WHERE competition_id=? ORDER BY score DESC", (cid,)).fetchall()
    return render_template("leaderboard.html", projects=projects, cid=cid, comp_name=comp['name'], user=get_user())

@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"].strip()
    db = get_db()
    db.execute("INSERT INTO competition (name) VALUES (?)", (name,))
    db.commit()
    return redirect(url_for('index'))

@app.route("/delete/<int:cid>", methods=["POST"])
def delete_competition(cid):
    db = get_db()
    db.execute("DELETE FROM project WHERE competition_id=?", (cid,))
    db.execute("DELETE FROM competition WHERE id=?", (cid,))
    db.commit()
    return redirect(url_for('index'))

@app.route("/disqualify/<int:pid>", methods=["POST"])
def disqualify(pid):
    db = get_db()
    project = db.execute("SELECT * FROM project WHERE id=?", (pid,)).fetchone()
    if project and project['submission_type'] == 'folder':
        path = os.path.join(app.config['PROJECT_FOLDER'], project['submission_content'])
        if os.path.exists(path): shutil.rmtree(path)
    db.execute("DELETE FROM project WHERE id=?", (pid,))
    db.commit()
    return redirect(request.referrer)

@app.route("/download_all/<int:cid>")
def download_all(cid):
    db = get_db()
    projects = db.execute("SELECT * FROM project WHERE competition_id=? AND submission_type='folder'", (cid,)).fetchall()
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for p in projects:
            path = os.path.join(app.config['PROJECT_FOLDER'], p['submission_content'])
            for root, dirs, files in os.walk(path):
                for file in files:
                    zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(app.config['PROJECT_FOLDER'])))
    memory_file.seek(0)
    return send_file(memory_file, download_name=f"comp_{cid}_projects.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)