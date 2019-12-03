from App.Actor import Actor

class User(Actor):
	id = 0
	name = ""
	lock = False

	user = {}

	def __init__(self, UserDAO):
		self.user = UserDAO
		self.sess_key = "user" # session key

	def list(self):
		user_list = self.user.list()

		return user_list

	def signin(self, email, password):
		user = self.user.get(email)

		if user is None:
			return False

		if user[3] != password:
			return False

		return user