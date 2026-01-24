from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock Database (In a real app, use SQLAlchemy or SQLite)
competitions = [] # Format: [id, name]
projects = []     # Format: {'id': 0, 'cid': 0, 'student': '', 'title': '', 'score': 0}

@app.route('/')
def index():
    return render_template('index.html', competitions=enumerate([c for c in competitions]))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        competitions.append(name)
        return redirect(url_for('index'))
    return render_template('create_competition.html')

@app.route('/submit/<int:cid>', methods=['GET', 'POST'])
def submit(cid):
    if request.method == 'POST':
        student = request.form.get('student')
        title = request.form.get('title')
        projects.append({'id': len(projects), 'cid': cid, 'student': student, 'title': title, 'score': 0})
        return redirect(url_for('index'))
    return render_template('submit_project.html')

@app.route('/judge/<int:cid>', methods=['GET', 'POST'])
def judge(cid):
    if request.method == 'POST':
        pid = int(request.form.get('pid'))
        score = int(request.form.get('score'))
        for p in projects:
            if p['id'] == pid:
                p['score'] = score
        return redirect(url_for('judge', cid=cid))
    
    # Filter projects for this specific competition
    comp_projects = [p for p in projects if p['cid'] == cid]
    # Format for judge.html template: (id, cid, student, title, score)
    formatted_projects = [(p['id'], p['cid'], p['student'], p['title'], p['score']) for p in comp_projects]
    return render_template('judge.html', projects=formatted_projects)

@app.route('/leaderboard/<int:cid>')
def leaderboard(cid):
    # Filter and sort projects by score (descending)
    comp_projects = [p for p in projects if p['cid'] == cid]
    sorted_projects = sorted(comp_projects, key=lambda x: x['score'], reverse=True)
    return render_template('leaderboard.html', projects=sorted_projects)

if __name__ == '__main__':
    app.run(debug=True)
