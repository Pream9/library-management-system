from App.Actor import Actor

class User(Actor):
	id = 0
	name = ""
	lock = False

	user = {}

	def __init__(self, UserDAO):
		self.user = UserDAO
		self.key = "user" # session key

	def list(self):
		user_list = self.user.list()

		return user_list