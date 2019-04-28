from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form["rot"])
    base_text = str(request.form["text"])

    return rotate_string(base_text, rotation)

form = """
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
        <form method='POST'>
                <label>Rotate by:<type=text>
                    <input name="rot" type="text" value="0" />
                </label>
                    <textarea name="text"></textarea>
                </label>
        <input type="submit" />
    </body>
</html>
"""

app.run()