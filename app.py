from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/index.html')
def index():
	return render_template("index.html", title="Ajaj-About")

# @app.route('/index.html/<name>')
# def indexnm(name):
# 	return render_template("index.html", name=name)

@app.route('/about.html/r-list')
def indexrl():
	friends=["Sari", "Rabee3", "Hamza", "Amin", "Ribhy"]
	display=True
	return render_template("about.html", display=display, list=friends)

@app.route('/hobbies.html')
def hobbies():
	return render_template("hobbies.html", title="Ajaj-Hobbies")

@app.route('/projects.html')
def projects():
	return render_template("projects.html", title="Ajaj-Projects")

@app.route('/about.html')
def about():
	return render_template("about.html", title="Ajaj-About")

@app.route('/contact.html')
def contact():
	return render_template("contact.html", title="Ajaj-Contact")















@app.route('/hello')
def hello():
	Quotes = ['The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart',
	 'Happiness is not something you postpone for the future; it is something you design for the present',
	  'Nothing is impossible, the word itself says I am possible!',
	  'Put your heart, mind, and soul into even your smallest acts. This is the secret of success',
	 'I cant change the direction of the wind, but I can adjust my sails to always reach my destination']
	return (random.choice(Quotes))

if __name__ == "__main__":
	app.run()