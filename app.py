from crypt import methods
from flask import Flask, render_template

from project.home import home_render
from project.signin import signin_render

app = Flask(__name__)

app.add_url_rule('/', view_func=home_render, methods=['get', 'post'])
app.add_url_rule('/index', view_func=home_render, methods=['get', 'post'])
app.add_url_rule('/home', view_func=home_render, methods=['get', 'post'])

app.add_url_rule('/signin', view_func=signin_render, methods=['get', 'post'])

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)