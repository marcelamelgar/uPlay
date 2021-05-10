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
    return render_template("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == 'POST':
        print("1")
        cardName = request.form["cname"]
        cardNum = request.form["ccnum"]
        expMonth = request.form["expmonth"]
        expYear = request.form["expyear"]
        cvv = request.form["cvv"]
        name = request.form["firstname"]
        email = request.form["email"]
        password = request.form["pass"]
        confirmPassword = request.form["cpass"]
        plan = request.form["plan"]
        birth = request.form["birth"]
        data = {}
        data['users'] = []
        data['users'].append({
            'cardName': cardName,
            'cardNum': cardNum,
            'expMonth': expMonth,
            'expYear': expYear,
            'cvv': cvv,
            'name': name,
            'email': email,
            'password': password,
            'confirmPassword': confirmPassword,
            'plan': plan,
            'birth': birth
        })
        with open('c:/Users/mepg1/Documents/GitHub/uPlay/prueba/users.json','w') as outfile:
            json.dump(data, outfile)
        return render_template("login.html")
    return render_template("signup.html")
    print("2")

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