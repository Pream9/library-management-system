class UserDAO():
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "users"


	def list(self):
		books = self.db.query("select * from @table").fetchall()

		return books