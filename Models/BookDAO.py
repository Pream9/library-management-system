class BookDAO():
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "books"

	def add_book():
		return "TBA"

	def list(self):
		books = self.db.query("select * from @table").fetchall()

		return books

	def search_book(self, name):
		q = self.db.query("select * from @table where name LIKE '%{}%'".format(name))
		books = q.fetchall()
		
		return books