from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO

from App.Books import Books
from App.User import User

book_manager = Blueprint('book_routes', __name__, template_folder='/templates')

books = Books(DAO.db.book)
user = User(DAO.db.user)

@book_manager.route('/books/', methods=['GET'])
def home():
	b = books.list()
	
	user.set_session(session, g)

	if b and len(b) <1:
		return render_template('books.html', error="No books found!")

	return render_template("books.html", books=b, g=g)


@book_manager.route('/books/add/<id>', methods=['GET'])
@user.login_required
def add(id):
	user_id = user.uid()
	books.reserve(user_id, id)

	b = books.list()
	user.set_session(session, g)
	
	return render_template("books.html", msg="Book reserved", books=b, g=g)


@book_manager.route('/books/search', methods=['GET'])
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

