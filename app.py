
from flask import Flask, render_template, url_for, request
from databases import *

app = Flask(__name__)

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/signin')
def signin():

	return render_template(
		'sign.html')

@app.route('/')
def mainpage():
	return render_template(
		'mainpage.html')

@app.route('/signup')
def signup():
	if request.method =='GET':
		return render_template(
		'signup.html')
	else:
		Email = request.form['Email']
		Password = request.form['Password']
		add_user(Email,Password)
		return render_template('home.html')




@app.route('/matharticle')

def matharticle():
	return render_template(
		'matharticle.html')

@app.route('/bioarticle')

def bioarticle():
	return render_template(
		'bioarticle.html')
@app.route('/submit')

def submit():
	return render_template(
		'submit.html')




if __name__ == '__main__':
    app.run(debug=True, port=3546)