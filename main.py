from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ='''
<!DOCTYPE html>

<html>
    <head>
        <style>
            .text {{
                text-align: center;
            }}
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <h1 class="text">Caesar Encryption</h1>
        <p class="text">just enter a number in the first box. <br/> 
        Then add your text in the second, push the encrypt button<br/>
        and voilá. Now the text is encrypted via caesar encryption</p>
      <form method="POST">
        <label>Rotate by
        <input type="text" name="rot" value="0"/>
        <label/>
        <textarea name="text">{0}</textarea>
        <input type="submit" value="encrypt"/>
      </form>
    </body>
</html>
'''


@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=["POST"])
def encrypt():
    encryptie = request.form["text"]
    rot = request.form["rot"]
    encrypted = rotate_string(encryptie, int(rot))
    return form.format(encrypted)

app.run()