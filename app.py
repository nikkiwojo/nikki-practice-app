from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "\U0001f47b NIKKI \U0001f47b"