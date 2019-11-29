from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO

from App.Books import Books
from App.Admin import Admin

admin_view = Blueprint('admin_routes', __name__, template_folder='/templates/admin/', url_prefix='/admin')

books = Books(DAO.books)
admin = Admin(DAO.admin)

@admin_view.route('/', methods=['GET'])
def home():
	# _admin.set_variables(session, g)

	return redirect('/admin/signin')

	return render_template('home.html', g=g)


@admin_view.route('/signin', methods=['GET', 'POST'])
def signin():
	g.bg = 1
	# _admin.set_variables(session, g)

	return render_template('admin/signin.html', g=g)