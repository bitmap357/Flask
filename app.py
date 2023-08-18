from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def home():
#     return '<h1>This is an index page</h1>'

# @app.route('/new')
# def new():
#     return '<h1>This is a new page</h1>'

# @app.route('/demo')
# def demo():
#     return '<h1>This is a demo page</h1>'


# @app.route('/profile/<int:id>')
# def profile(id):
#     return '<h1>This is a profile page for %d</h1>' % id


@app.route('/admin')
def welcome_admin():
    return 'Welcome admin'

app.run(debug=True)