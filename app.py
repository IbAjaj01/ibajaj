from flask import Flask, render_template, request
import dataset
import random
app = Flask(__name__)
db = dataset.connect("postgres://afoannpojeexms:a84ab8f3f4296172e4e2b9b0189adf00fe94705efb17ccbb5d96196a01941f4a@ec2-23-21-96-70.compute-1.amazonaws.com:5432/d5cs30nlpgtp86")

@app.route('/home')
def index():
	return render_template("index.html", title="Ajaj-Home")

# @app.route('/formExample', methods=["GET", "POST"])
# def formExmaple():
# 	if request.method == "GET":
# 		return render_template("contact.html")
# 	else:
# 		form = request.form
# 		userName = form["username"]
# 		email = form["email"]
# 		subject = form["subject"]
# 		return render_template("contact.html", username=username, emailValue=emailValue, subjectValue=subjectValue)


# @app.route('/index.html/listExamples', methods=["POST"])
# def indexnm(name):
# 	displayContent = request.form["displayContent"]
# 	print(displayContent)
# 	display = 


# @app.route('/about.html/r-list')
# def indexrl():
# 	friends=["Sari", "Rabee3", "Hamza", "Amin", "Ribhy"]
# 	display=True
# 	return render_template("about.html", display=display, list=friends)

@app.route('/hobbies')
def hobbies():
	return render_template("hobbies.html", title="Ajaj-Hobbies")

@app.route('/projects')
def projects():
	return render_template("projects.html", title="Ajaj-Projects")

@app.route('/about')
def about():
	return render_template("about.html", title="Ajaj-About")

@app.route('/contact')
def contact():
	return render_template("contact.html", title="Ajaj-Contact")




@app.route('/db', methods=["POST"])
def showContact():
	form = request.form
	name = form["userName"]
	email = form["email"]
	subject = form["subject"]
	contactsTable = db["contacts"]
	entry = {"name":name, "email":email, "subject":subject}
	contactsTable.insert(entry)
	print list(contactsTable.all())

	return render_template("show.html", name=name, email=email, subject=subject)

# @app.route('/showusers')
# def showAll():
# 	contacts = db["contact"]
# 	allcontacts = list(contacts.all())
# 	return render_template("show.html", contacts=allcontacts)








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