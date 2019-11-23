from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

# @app.route('/')
# def index():
#     response = make_response('<h1>This is document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response

# @app.route('/')
# def index():
#     return redirect('http://www.example.com')

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}!</h1>'.format(user.name)
