from App.Actor import Actor

class User(Actor):
	id = 0
	name = ""
	lock = False

	user = {}

	def __init__(self, UserDAO):
		self.user = UserDAO
		self.sess_key = "user" # session key

	def get(self, id):
		user = self.user.getById(id)

		return user

	def list(self):
		user_list = self.user.list()

		return user_list

	def signin(self, email, password):
		user = self.user.getByEmail(email)

		if user is None:
			return False

		user_pass = user[3] # user pass at 
		if user_pass != password:
			return False

		return user

	def signup(self, name, email, password):
		user = self.user.getByEmail(email)

		if user is not None:
			return "already_exists"

		user_info = {"name": name, "email": email, "password": password}
		
		new_user = self.user.add(user_info)

		return new_user