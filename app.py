from flask import Flask, redirect, url_for, request, render_template

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


# @app.route('/admin')
# def welcome_admin():
#     return 'Welcome admin'

# @app.route('/guest/<guest>')
# def welcome_guest(guest):
#     return 'Welcome guest, %s' % guest

# @app.route('/user/<name>')
# def welcome_user(name):
#     if name == 'admin':
#         return redirect(url_for('welcome_admin'))
#     else:
#         return redirect(url_for('welcome_guest', guest=name))


# @app.route('/')
# def index():
#     return 'This is a request made by the client %s' % request.headers


@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

@app.route('/submitbook', methods=['POST'])
def submitbook():
    name = request.form['name']
    author = request.form['author']

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