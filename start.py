from flask import Flask, render_template

app = Flask(__name__, template_folder='./frontend')

@app.route("/")
def start():
    return render_template('home.html')