class UserDAO():
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "users"


	def list(self):
		users = self.db.query("select * from @table").fetchall()

		return users

	def get(self, email):
		q = self.db.query("select * from @table where email='%s'".format(email))

		user = q.fetch()
		return user