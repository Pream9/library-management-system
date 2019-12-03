from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO

from App.Books import Books
from App.Admin import Admin

admin_manager = Blueprint('admin_routes', __name__, template_folder='../templates/admin/', url_prefix='/admin')

books = Books(DAO.db.books)
admin = Admin(DAO.db.admin)


@admin_manager.route('/', methods=['GET'])
@admin.login_required
def home():
	admin.set_session(session, g)

	return render_template('admin/home.html', g=g)


@admin_manager.route('/signin/', methods=['GET', 'POST'])
@admin.redirect_if_login
def signin():
	g.bg = 1
	return render_template('admin/signin.html', g=g)


@admin_manager.route('/books/', methods=['GET'])
@admin.login_required
def books():
	return render_template('books/view.html', g=g)


@admin_manager.route('/books/add', methods=['GET', 'POST'])
@admin.login_required
def book_add():
	return render_template('books/add.html', g=g)


@admin_manager.route('/books/edit', methods=['GET', 'PUT'])
@admin.login_required
def book_edit():
	return render_template('books/edit.html', g=g)

@admin_manager.route('/books/edit', methods=['DELETE'])
@admin.login_required
def book_delete():
	return render_template('books/edit.html', g=g)