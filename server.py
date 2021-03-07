from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

domain = "0.0.0.0:5000/"
number = 0
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)