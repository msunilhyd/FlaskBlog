from flaskBlog import db, login_manager, admin
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))




class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)	
	content = db.Column(db.Text, nullable=False)
	post_image_file = db.Column(db.String(30))	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "Post('{}','{}''{}')".format(self.title, self.date_posted, self.user_id)


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	email = db.Column(db.String(50), unique=True, nullable=False)	
	image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
	password = db.Column(db.String(100), nullable=False)
	tests = db.relationship('Test', backref='author', lazy=True)
	posts = db.relationship('Post', backref='author', lazy=True)
	is_admin = db.Column(db.Integer, nullable=False, default=0)

	
	def get_id(self):
		return (self.id)

	def __repr__(self):
		return "User('{}', '{}', '{}')".format(self.username, self.email, self.image_file)



class Test(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	test_name = db.Column(db.String(50), nullable=False)
	category = db.Column(db.String(50))
	instructions = db.Column(db.String(1000), nullable=False)
	no_of_questions = db.Column(db.Integer, nullable=False)
	total_marks = db.Column(db.Integer, nullable=False)
	time_in_mins = db.Column(db.Integer, nullable=False, default=180)
	date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "Test('{}','{}''{}')".format(self.id,self.test_name, self.category, self.no_of_questions, self.user_id)

class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	section = db.Column(db.String(100), nullable=False)
	question_content = db.Column(db.String(500), nullable=False)
	a = db.Column(db.String(100), nullable=False)
	b = db.Column(db.String(100), nullable=False)
	c = db.Column(db.String(100), nullable=False)
	d = db.Column(db.String(100), nullable=False)
	ans = db.Column(db.String(100), nullable=False)
	positive_marks = db.Column(db.Integer, nullable=False)
	negative_marks = db.Column(db.Integer, nullable=False)
	date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)	

	def __repr__(self):
		return "Question('{}','{}''{}')".format(self.id, self.question_content, self.positive_marks)

class TestQuestion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
	questions = db.relationship('Question', backref='NameOfTest', lazy=True)
	
	def __repr__(self):
		return "TestQuestion('{}','{}')".format(self.test_id, self.id)


class UserTest(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user_score = db.Column(db.Integer, nullable=False, default=0)
	positive_score = db.Column(db.Integer, nullable=False, default=0)
	negative_score = db.Column(db.Integer, nullable=False, default=0)
	correct_answers = db.Column(db.Integer, nullable=False, default=0)
	wrong_answers = db.Column(db.Integer, nullable=False, default=0)
	no_answers = db.Column(db.Integer, nullable=False, default=0)
	test_taken_on_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)	
	__table_args__ = (db.UniqueConstraint('test_id', 'user_id'), )

	def __repr__(self):
		return "UserTest('{}','{}''{}')".format(self.id, self.test_id, self.user_id, self.user_score)



admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Test, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(TestQuestion, db.session))
admin.add_view(ModelView(UserTest, db.session))
