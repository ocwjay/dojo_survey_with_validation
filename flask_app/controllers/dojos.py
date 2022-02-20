from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info_submission', methods=['POST'])
def submit_info():
    if not Dojo.validate_survey(request.form['name'], request.form['location'], request.form['fav_language'], request.form['comments']):
        return redirect('/')
    data = {
    'name' : request.form['name'],
    'location' : request.form['location'],
    'language' : request.form['fav_language'],
    'comment' : request.form['comments']
    }
    survey = Dojo.submit_survey(data)
    return redirect(f'/results/{survey}')

@app.route('/results/<int:id>')
def show_results(id):
    data = {
        'id' : id
    }
    return render_template('results.html', survey = Dojo.get_survey(data))