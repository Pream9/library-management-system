from flask import Flask, render_template, request, jsonify, Response
from db import DB

app = Flask(__name__)
db = DB(app)

@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/user/<username>')
def show_user(username=None):
	q = db.query("select name,email,height from users where name='%s'"%username)
	d = q.fetchone()
	return render_template("profile.html", user=d)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post #%i" % post_id

# if __name__=='__main__':
# 	app.run(host='0.0.0.0',port=3333,debug=True)