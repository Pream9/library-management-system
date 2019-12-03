from App.Actor import Actor

class Admin(Actor):
	admin = {}
	
	def __init__(self, AdminDAO):
		self.sess_key = "admin"
		self.admin = AdminDAO
		self.route_url = "/admin/"

	def signin(self):
		pass