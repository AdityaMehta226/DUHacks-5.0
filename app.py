from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock Database (In-memory storage)
competitions = [] 
projects = []     

@app.route('/')
def index():
    # enumerate provides (index, competition_name)
    return render_template('index.html', competitions=enumerate(competitions))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            competitions.append(name)
        return redirect(url_for('index'))
    return render_template('create_competition.html')

@app.route('/submit/<int:cid>', methods=['GET', 'POST'])
def submit(cid):
    if request.method == 'POST':
        student = request.form.get('student')
        title = request.form.get('title')
        if student and title:
            projects.append({
                'id': len(projects), 
                'cid': cid, 
                'student': student, 
                'title': title, 
                'score': 0
            })
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
    
    comp_projects = [(p['id'], p['cid'], p['student'], p['title'], p['score']) 
                     for p in projects if p['cid'] == cid]
    return render_template('judge.html', projects=comp_projects)

@app.route('/leaderboard/<int:cid>')
def leaderboard(cid):
    comp_projects = [p for p in projects if p['cid'] == cid]
    sorted_projects = sorted(comp_projects, key=lambda x: x['score'], reverse=True)
    
    # Matches the indexing expected by your leaderboard.html
    formatted_projects = [[p['title'], p['student'], p['score']] for p in sorted_projects]
    return render_template('leaderboard.html', projects=formatted_projects)

if __name__ == '__main__':
    app.run(debug=True)