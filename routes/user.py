from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO

from App.Books import Books
from App.User import User

user_view = Blueprint('user_routes', __name__, template_folder='/templates')

books = Books(DAO.db.books)
user = User(DAO.db.user)

@user_view.route('/', methods=['GET'])
def home():
	g.bg = 1

	user.set_session(session, g)

	return render_template('home.html', g=g)


@user_view.route('/books', methods=['GET'])
def show_books():
	b = books.list()
	
	user.set_session(session, g)

	if b and len(b) <1:
		return render_template('books.html', error="No books found!")

	return render_template("books.html", books=b, g=g)


@user_view.route('/books/search', methods=['GET'])
def search():
	user.set_session(session, g)

	if "keyword" not in request.args:
		return render_template("search.html")

	keyword = request.args["keyword"]

	if len(keyword)<1:
		return redirect('/books')

	d=books.search(keyword)

	if len(d) >0:
		return render_template("books.html", search=True, books=d, count=len(d), keyword=escape(keyword), g=g)

	return render_template('books.html', error="No books found!", keyword=escape(keyword))



@user_view.route('/signin', methods=['GET', 'POST'])
@user.redirect_if_login
def signin():
	# Show login view
	if user.isLoggedIn(session):
		return redirect('/')

	if request.method == 'POST':
		_form = request.form
		email = str(_form["email"])
		password = str(_form["password"])

		if len(email)<1 or len(password)<1:
			return render_template('signin.html', error="Email and password are required")

		d = user.signin(email, password)

		if d and len(d)>0:
			session['user'] = int(d[0])

			return redirect("/")

		return render_template('signin.html', error="Email or password incorrect")


	return render_template('signin.html')


@user_view.route('/signup', methods=['GET', 'POST'])
@user.redirect_if_login
def signup():
	# Show signup view
	if user.isLoggedIn(session):
		return redirect('/')

	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		password = request.form.get('password')

		print("Register")

		return render_template('signup.html')


	return render_template('signup.html')


@user_view.route('/signout', methods=['GET'])
@user.login_required
def signout():
	session["user"] = 0

	return redirect("/", code=302)

@user_view.route('/user/<id>', methods=['GET'])
@user.login_required
def show_user(id=None):
	if not user.isLoggedIn(session):
		return redirect('/signin')

	user.set_session(session, g)
	
	if id is None:
		id = session["user"]

	d = user.get_info(int(id))

	return render_template("profile.html", user=d, g=g)