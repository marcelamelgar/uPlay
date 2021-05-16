from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
import json

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["GET","POST"])   
def login():
    if request.method == 'POST':
        email = request.form["username"]
        password = request.form["password"]
        with open("c:/Users/mepg1/Documents/GitHub/uPlay/prueba/users.json") as json_file:
            my_json = json.load(json_file)
        for i in my_json["Users"]:
            values = list(i.values())
            if values[1] == email and values[2] == password:
                return render_template("inicio.html")
    return render_template("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == 'POST':
        cardName = request.form["cardname"]
        cardNum = request.form["cardnumber"]
        expMonth = request.form["expmonth"]
        expYear = request.form["expyear"]
        cvv = request.form["cvv"]
        name = request.form["firstname"]
        email = request.form["email"]
        password = request.form["password"]
        confirmPassword = request.form["confirmpassword"]
        plan = request.form["plan"]
        birth = request.form["birth"]
        with open("c:/Users/mepg1/Documents/GitHub/uPlay/prueba/users.json") as json_file:
            my_json = json.load(json_file)
            my_json["Users"].append({"name":name,"email":email,"password":password,"plan":plan,"birth":birth,"cardName":cardName,"cardNum":cardNum,"expMonth":expMonth,"expYear":expYear,"cvv":cvv})
        with open('c:/Users/mepg1/Documents/GitHub/uPlay/prueba/users.json','w') as outfile:
            json.dump(my_json, outfile)
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route("/terms", methods=["GET","POST"])
def terms():
    return render_template("terms.html")

@app.route("/rpassword", methods=["GET","POST"])
def rpassword():
    return render_template("rpassword.html")

@app.route("/inicio", methods={"GET","POST"})
def inicio():
    return render_template("inicio.html")

@app.route("/music", methods={"GET","POST"})
def music():
    return render_template("indexMusic.html")

@app.route("/movies", methods={"GET","POST"})
def movies():
    return render_template("indexMovies.html")

@app.route("/mymusic", methods={"GET","POST"})
def mymusic():
    return render_template("mymusic.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)