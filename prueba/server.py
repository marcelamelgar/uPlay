from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

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