import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- DATABASE SETUP ---
DATABASE = 'hackathon.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS competitions 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS projects 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, cid INTEGER, 
                         student TEXT, title TEXT, score INTEGER DEFAULT 0)''')
    print("Database initialized!")

# Initialize the DB when the app starts
if not os.path.exists(DATABASE):
    init_db()

# --- ROUTES ---

@app.route('/')
def index():
    conn = get_db()
    comps = conn.execute('SELECT * FROM competitions').fetchall()
    conn.close()
    return render_template('index.html', competitions=comps)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            conn = get_db()
            conn.execute('INSERT INTO competitions (name) VALUES (?)', (name,))
            conn.commit()
            conn.close()
        return redirect(url_for('index'))
    return render_template('create_competition.html')

@app.route('/submit/<int:cid>', methods=['GET', 'POST'])
def submit(cid):
    if request.method == 'POST':
        student = request.form.get('student')
        title = request.form.get('title')
        conn = get_db()
        conn.execute('INSERT INTO projects (cid, student, title) VALUES (?, ?, ?)', 
                     (cid, student, title))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('submit_project.html', cid=cid)

@app.route('/judge/<int:cid>', methods=['GET', 'POST'])
def judge(cid):
    conn = get_db()
    if request.method == 'POST':
        pid = request.form.get('pid')
        score = request.form.get('score')
        conn.execute('UPDATE projects SET score = ? WHERE id = ?', (score, pid))
        conn.commit()
    
    comp_projects = conn.execute('SELECT * FROM projects WHERE cid = ?', (cid,)).fetchall()
    conn.close()
    return render_template('judge.html', projects=comp_projects, cid=cid)

@app.route('/leaderboard/<int:cid>')
def leaderboard(cid):
    conn = get_db()
    sorted_projects = conn.execute('''SELECT * FROM projects WHERE cid = ? 
                                      ORDER BY score DESC''', (cid,)).fetchall()
    conn.close()
    return render_template('leaderboard.html', projects=sorted_projects)

# --- DEPLOYMENT SETTINGS ---
if __name__ == '__main__':
    # host='0.0.0.0' is required for Render
    # port=int(os.environ.get("PORT", 10000)) ensures Render can assign a port
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
