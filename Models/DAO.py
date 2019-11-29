from copy import copy

from Models.BookDAO import BookDAO
from Models.UserDAO import UserDAO
from Models.AdminDAO import AdminDAO

from Models.DB import DB

class DAO(DB):
	def __init__(self, app):
		super(DAO, self).__init__(app)

		self.books = BookDAO(copy(self))
		self.user = UserDAO(copy(self))
		self.admin = AdminDAO(copy(self))
