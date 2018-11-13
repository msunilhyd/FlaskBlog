from flask import render_template, url_for, flash, redirect
from flaskBlog import app, db, bcrypt
from flaskBlog.forms import RegistrationForm, LoginForm
from flaskBlog.models import User, Post


posts = [
	{
		'author' : 'Sunil Mocharla',
		'title' : 'Blog Post 1',
		'content' : 'First post content',
		'date_posted' : 'April 20, 2014'
	},
	{
		'author' : 'Prash Jajjari',
		'title' : 'Blog Post 2',
		'content' : 'Second post content',
		'date_posted' : 'May 31, 2014'
	}

]


@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email = form.email.data, password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your Account has been created ! You should be able to Login', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@admin.com' and form.password.data == 'admin':
			flash('You have been logged in !', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful, Check username and password', 'danger')

	return render_template('login.html', title='Login', form=form)
