from flask import Flask, request, redirect, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("caesar.html")

@app.route("/", methods=["POST"])
def encrypt():
    encryptie = request.form["text"]
    rot = request.form["rot"]
    encrypted = rotate_string(encryptie, int(rot))
    return render_template("caesar.html", encrypt=encrypted)

app.run()