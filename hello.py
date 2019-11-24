from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstarp = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # return render_template('user.html', name=name)
    return render_template('user.html', name=name)
