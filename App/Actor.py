class Actor():
	key = ""

	def set_session(self, session, g):
		g.user = 0

		if self.isLoggedIn(session):
			g.user = session[self.key]

	def isLoggedIn(self, session):
		if self.key in session and session[self.key]>0:
			return True

		return False