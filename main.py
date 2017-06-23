from flask import Flask, request, redirect, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST", "GET"])
def encrypt():
    if request.method == 'POST':
        encryptie = request.form["text"]
        rot = request.form["rot"]
        encrypted = rotate_string(encryptie, int(rot))
        return render_template("caesar.html", encrypt=encrypted)
    if request.method == 'GET':
        return render_template("caesar.html")

app.run()