from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO

from App.User import User
from App.Books import Books

user_manager = Blueprint('user_routes', __name__, template_folder='/templates')

user = User(DAO.db.user)
books = Books(DAO.db.book)

@user_manager.route('/', methods=['GET'])
def home():
	g.bg = 1

	user.set_session(session, g)

	return render_template('home.html', g=g)


@user_manager.route('/signin', methods=['GET', 'POST'])
@user.redirect_if_login
def signin():
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


@user_manager.route('/signup', methods=['GET', 'POST'])
@user.redirect_if_login
def signup():
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		password = request.form.get('password')

		if len(name) < 1 or len(email)<1 or len(password)<1:
			return render_template('signup.html', error="All fields are required")

		new_user = user.signup(name, email, password)

		if new_user == "already_exists":
			return render_template('signup.html', error="User already exists with this email")


		return render_template('signup.html', msg = "You've been registered!")


	return render_template('signup.html')


@user_manager.route('/signout/', methods=['GET'])
@user.login_required
def signout():
	user.signout()

	return redirect("/", code=302)

@user_manager.route('/user/', methods=['GET'])
@user.login_required
def show_user(id=None):
	user.set_session(session, g)
	
	if id is None:
		id = int(user.uid())

	d = user.get(id)
	mybooks = books.getUserBooks(id)

	return render_template("profile.html", user=d, books=mybooks, g=g)