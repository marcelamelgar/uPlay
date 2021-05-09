from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from linkedlist import Cancion, Album, Artist
import json

canciones = []
albumes = []
artistas = []
contadorCanciones = 0
contadorAlbumes = 0
contadorArtistas = 0

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

def cargarCanciones():
    with open("c:/Users/mepg1/Documents/GitHub/uPlay/prueba/music.json") as json_file:
        my_json = json.load(json_file)
    for i in my_json["songs"]:
        canciones.append(Cancion(i.name,i.artist,i.album))
        contadorCanciones += 1

def cargarAlbumes():
    with open("c:/Users/mepg1/Documents/GitHub/uPlay/prueba/albums.json") as json_file:
        my_json = json.load(json_file)
    for i in my_json["albumes"]:
        albumes.append(Album(i.name,i.artist,i.album))
        contadorAlbumes += 1

def cargarCanciones():
    with open("c:/Users/mepg1/Documents/GitHub/uPlay/prueba/artists.json") as json_file:
        my_json = json.load(json_file)
    for i in my_json["artists"]:
        artistas.append(Artist(i.name,i.artist,i.album))
        contadorArtistas += 1

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


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)