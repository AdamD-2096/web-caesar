from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ='''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="POST">
        <label>Rotate by
        <input type="text" name="rot" value="0"/>
        <label/>
        <input type="textarea" name="text"/>
        <input type="submit"/>
      </form>
    </body>
</html>
'''


@app.route("/")
def index():
    return form#.format(encryption='')

@app.route("/", methods=["POST"])
def encrypt():
    encryptie = request.form["text"]
    rot = request.form["rot"]
    encrypted = rotate_string(encryptie, int(rot))
    return "<h1>{0}<h1>".format(encrypted)

app.run()