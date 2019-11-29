class AdminDAO():
	db = {}
	
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "admin"