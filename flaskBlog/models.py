from flaskBlog import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func



@login_manager.user_loader
def load_user(userid):
	return User.query.get(int(userid))


class User(db.Model, UserMixin):
	userid = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(20), unique=True, nullable=False)	
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	
	def get_id(self):
		return (self.userid)

	def __repr__(self):
		return "User('{}', '{}', '{}')".format(self.username, self.email, self.image_file)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)	
	content = db.Column(db.Text, nullable=False)
	post_image_file = db.Column(db.String(30))	
	user_id = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False)

	def __repr__(self):
		return "Post('{}','{}''{}')".format(self.title, self.date_posted, self.user_id)


