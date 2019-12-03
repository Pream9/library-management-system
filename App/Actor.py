from functools import wraps
from flask import g, request, redirect, session

class Actor():
	sess_key = ""
	route_url = "/"

	def set_session(self, session, g):
		g.user = 0

		if self.isLoggedIn(session):
			g.user = session[self.sess_key]

	def isLoggedIn(self, session):
		if self.sess_key in session and session[self.sess_key]>0:
			return True

		return False

	def login_required(self, f, path="signin"):
		@wraps(f)
		def decorated_function(*args, **kwargs):
		    if self.sess_key not in session or session[self.sess_key] is None:
		        return redirect(self.route_url+path)
		    return f(*args, **kwargs)
		return decorated_function

	def redirect_if_login(self, f, path="/"):
		@wraps(f)
		def decorated_function(*args, **kwargs):
		    if self.sess_key in session:
		        return redirect(self.route_url+path)
		    return f(*args, **kwargs)
		return decorated_function

	def signout():
		session[self.sess_key] = None

	def signin():
		pass