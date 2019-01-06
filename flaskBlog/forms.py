from flask_wtf import FlaskForm

from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskBlog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):

	username = StringField('Username', 
						validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', 
						validators=[DataRequired(), Email()] )
	password = PasswordField('Password', 
						validators=[DataRequired()] )
	confirm_password = PasswordField('Confirm Password',
						validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('That username is already taken, Please choose a different one')


	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user:
			raise ValidationError('That email is already taken, Please choose a different one')


class LoginForm(FlaskForm):

	email = StringField('Email', 
						validators=[DataRequired(),Email()] )
	password = PasswordField('Password', 
						validators=[DataRequired()] )
	remember = BooleanField('Remember Me')
	submit = SubmitField('Log in')



class UpdateAccountForm(FlaskForm):

	username = StringField('Username', 
						validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', 
						validators=[DataRequired(), Email()] )
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username = username.data).first()
			if user:
				raise ValidationError('That username is already taken, Please choose a different one')


	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email = email.data).first()
			if user:
				raise ValidationError('That email is already taken, Please choose a different one')



class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	picture = FileField('Upload Post Picture', validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField('Post')



class TestForm(FlaskForm):
	test_name = StringField('Test Name', validators=[DataRequired()])
	category = StringField('Test category')
	no_of_questions = IntegerField('Total No:of Questions', validators=[DataRequired()])
	total_marks = IntegerField('Total Marks', validators=[DataRequired()])
	time_in_mins = IntegerField('Test time in Minutes', validators=[DataRequired()])
	submit = SubmitField('Submit')
