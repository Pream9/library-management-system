class Books():
	id = 0
	name = ""
	edition = ""
	year = ""
	count = 0
	availability = False

	course = {}

	def __init__(self, BookDAO):
		self.books = BookDAO

	def list(self):
		book_list = self.books.list()

		return book_list

	def search(self, keyword):
		books = self.books.search_book(keyword)

		return books

	def reserve(self, user_id, book_id):
		books = self.books.reserve(user_id, book_id)

		return books

	def getUserBooks(self, user_id):
		books = self.books.getBooksByUser(user_id)

		return books
