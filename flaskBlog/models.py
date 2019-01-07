from flaskBlog import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func



@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(20), unique=True, nullable=False)	
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	tests = db.relationship('Test', backref='author', lazy=True)
	posts = db.relationship('Post', backref='author', lazy=True)
	testQuestions = db.relationship('TestQuestion', backref='author', lazy=True)
	
	def get_id(self):
		return (self.id)

	def __repr__(self):
		return "User('{}', '{}', '{}')".format(self.username, self.email, self.image_file)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)	
	content = db.Column(db.Text, nullable=False)
	post_image_file = db.Column(db.String(30))	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "Post('{}','{}''{}')".format(self.title, self.date_posted, self.user_id)


class Test(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	test_name = db.Column(db.String(30), nullable=False)
	category = db.Column(db.String(30))
	no_of_questions = db.Column(db.Integer, nullable=False)
	total_marks = db.Column(db.Integer, nullable=False)
	time_in_mins = db.Column(db.Integer, nullable=False, default=180)
	date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "Test('{}','{}''{}')".format(self.test_name, self.category, self.no_of_questions, self.user_id)

class TestQuestion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
	question = db.Column(db.String(500), nullable=False)
	a = db.Column(db.String(100), nullable=False)
	b = db.Column(db.String(100), nullable=False)
	c = db.Column(db.String(100), nullable=False)
	d = db.Column(db.String(100), nullable=False)
	ans = db.Column(db.String(100), nullable=False)
	positive_marks = db.Column(db.Integer, nullable=False)
	negative_marks = db.Column(db.Integer, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "TestQuestion('{}','{}''{}')".format(self.id, self.test_id, self.positive_marks, self.user_id)
