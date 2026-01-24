from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# This list starts empty and will grow as you add names
competitions = []

@app.route('/')
def home():
    return render_template('index.html', competitions=competitions)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        author = request.form.get('author')
        
        # Create a new dictionary for the competition
        new_comp = {
            "id": len(competitions) + 1,
            "name": name,
            "author": author,
            "score": 0
        }
        competitions.append(new_comp) # This adds it dynamically
        return redirect(url_for('home'))
        
    return render_template('create.html')

@app.route('/judge/<int:project_id>', methods=['GET', 'POST'])
def judge(project_id):
    project = next((p for p in competitions if p['id'] == project_id), None)
    if request.method == 'POST':
        score = request.form.get('score')
        if project:
            project['score'] = int(score)
        return redirect(url_for('leaderboard'))
    return render_template('judge.html', project=project)

@app.route('/leaderboard')
def leaderboard():
    sorted_projects = sorted(competitions, key=lambda x: x['score'], reverse=True)
    return render_template('leaderboard.html', projects=sorted_projects)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
