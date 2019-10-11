from flask_mysqldb import MySQL

class DB():
	"""Initialize mysql database """
	host = "hostname"
	user = "user";
	password = "password";
	db = "dbname";

	def __init__(self, app):
		app.config["MYSQL_HOST"] = self.host;
		app.config["MYSQL_USER"] = self.user;
		app.config["MYSQL_PASSWORD"] = self.password;
		app.config["MYSQL_DB"] = self.db;

		self.mysql = MySQL(app)

	def cur(self):
		return self.mysql.connection.cursor()

	def query(self, q):
		h = self.cur()
		h.execute(q)

		return h

