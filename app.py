from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>This is an index page</h1>'


app.run()