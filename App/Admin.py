from App.Actor import Actor

class Admin(Actor):
	admin = {}
	
	def __init__(self, AdminDAO):
		self.key = "admin"
		self.admin = AdminDAO
