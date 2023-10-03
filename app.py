from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "mydatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Book(db.Model):
    


@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

@app.route('/submitbook', methods=['POST'])
def submitbook():
    name = request.form['name']
    author = request.form['author']
    return 'Book name is %s and author is %s' % (name,author)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    
    return render_template('profile.html', username=username, isActive = True)

# @app.route('/books')
# def books():
#     books = ['Book1', 'Book2', 'Book3']
#     return render_template('books.html', books=books)

@app.route('/books')
def books():
    books = [{'name':'Book1', 'author': 'Author1', 'cover':'https://designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg'},
             {'name':'Book2', 'author': 'Author2', 'cover':'https://designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg'},
             {'name':'Book3', 'author': 'Author3', 'cover':'https://designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg'}]
    return render_template('books.html', books=books)

app.run(debug=True) 