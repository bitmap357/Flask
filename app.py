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
    name = db.Column(db.String(100),unique=True,
                     nullable=False, primary_key=True)
    author = db.Column(db.String(100),
                       nullable=False)


@app.route('/updatebooks')
def updatebooks():
    books = Book.query.all()
    return render_template('updatebooks.html', books=books)


@app.route('/update', methodS=['POST'])
def update():
    newname = request.form['newname']
    oldname = request.form['oldname']
    newauthor = request.form['newauthor']
    
    book = Book.query.filter_by(name=oldname).first()
    book.name = newname
    book.author = newauthor
    db.session.commit()
    return redirect('/books')

@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

@app.route('/submitbook', methods=['POST'])
def submitbook():
    name = request.form['name']
    author = request.form['author']
    book = Book(name=name, author=author)
    db.session.add(book)
    db.session.commit()
    return redirect('/books')

@app.route('/')
def index():
    with app.app_context():
        pass
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    
    return render_template('profile.html', username=username, isActive = True)

@app.route('/books')
def books():
    books = Book.query.all() 
    return render_template('books.html', books=books)

# @app.route('/books')
# def books():
#     books = [{'name':'Book1', 'author': 'Author1', 'cover':'https://designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg'},
#              {'name':'Book2', 'author': 'Author2', 'cover':'https://designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg'},
#              {'name':'Book3', 'author': 'Author3', 'cover':'https://designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg'}]
#     return render_template('books.html', books=books)

if __name__ == "__main__":
    app.run(debug=True) 