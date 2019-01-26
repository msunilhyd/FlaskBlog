import os
import secrets
from flask import render_template, url_for, flash, redirect, json,request, abort,jsonify, json, Markup
from flaskBlog import app, db, bcrypt, mysql
from flaskBlog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, TestForm, TestQuestionForm
from flaskBlog.models import User, Post, Test, TestQuestion, Question, UserTest
from flask_login import login_user, current_user, logout_user, login_required
from flask_json import FlaskJSON, JsonError, json_response, as_json
import re

		

@app.route("/")
def main():
	tests = Test.query.order_by(Test.date_posted.desc())
	return render_template('alltests.html', tests=tests)

@app.route("/user/<string:username>")
def user_posts(username):	
	page = request.args.get('page', 1, type=int)
	user = User.query.filter_by(username=username).first_or_404()
	posts = Post.query\
				.filter_by(author=user)\
				.order_by(Post.date_posted.desc())\
				.paginate(page=page, per_page=5)
	return render_template('user_posts.html', posts=posts, user=user)

@app.route("/home")
def home():	
	tests = Test.query.order_by(Test.date_posted.desc())
	return render_template('alltests.html', tests=tests)


@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email = form.email.data, password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your Account has been created ! You should be able to Login', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return render_template('quiz2Exp.html', title='Register')
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful, Check email and password', 'danger')

	return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
	logout_user()
	return render_template('home.html')



def save_profile_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
	form_picture.save(picture_path)

	return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_profile_picture(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()	
		flash('Your Account has been Updated !', 'success')
		return redirect(url_for('account'))		
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email	
	image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
	return render_template('account.html', title="Account", image_file=image_file, form=form)


def save_post_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/post_pics', picture_fn)
	form_picture.save(picture_path)

	return picture_fn

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_post_picture(form.picture.data)
			post = Post(title=form.title.data, content=form.content.data, author=current_user, post_image_file=picture_file)
		else :
			post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		flash("You post has been created", "success")
		return redirect(url_for('home'))
	return render_template('create_post.html', title="New Post", form=form, legend='New Post')


@app.route("/test/new", methods=['GET', 'POST'])
@login_required
def new_test():
	form = TestForm()
	if form.validate_on_submit():
		instrString = form.instructions.data.replace('\r', '').replace('\n', '<br>')
		test = Test(test_name=form.test_name.data, category=form.category.data, no_of_questions=form.no_of_questions.data, instructions=instrString,total_marks=form.total_marks.data, time_in_mins=form.time_in_mins.data, author=current_user)
		db.session.add(test)
		db.session.commit()
		test = Test.query.filter_by(test_name=form.test_name.data).order_by(Test.date_posted.desc()).first()

		flash("You test has been created", "success")
		return redirect(url_for('new_test_question', test_id=test.id))

	return render_template('create_test.html', title="New Test", form=form, legend='New test')



@app.route("/new_test_question/<int:test_id>", methods=['GET', 'POST'])
@login_required
def new_test_question(test_id):
	form = TestQuestionForm()
	if form.validate_on_submit():
		current_question = Question(section=form.section.data,question_content=form.question_content.data, a=form.a.data, b=form.b.data, c=form.c.data, d=form.d.data, ans=form.ans.data,positive_marks=form.positive_marks.data, negative_marks=form.negative_marks.data)
		db.session.add(current_question)
		db.session.commit()
		question = Question.query.filter_by(question_content=form.question_content.data).order_by(Question.date_posted.desc()).first()
		flash("You Question has been created", "success")
		testQuestion = TestQuestion(test_id=test_id, question_id=question.id)
		db.session.add(testQuestion)
		db.session.commit()
		return redirect(url_for('tests'))
	return render_template('create_test_questions.html', title="New Test Question", form=form, legend='New test Question')


@app.route("/tests")
def tests():	
	tests = Test.query.order_by(Test.date_posted.desc())
	return render_template('alltests.html', tests=tests)

@app.route("/test/<int:test_id>")
def test(test_id):
	user_id = request.args.get('user_id', None)
	test = Test.query.get_or_404(test_id)	
	usertest = UserTest.query.filter_by(test_id=test_id, user_id=user_id).first()

	return render_template('test.html', test=test, usertest=usertest)

@app.route("/post/<int:post_id>")
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('post.html', title=post.title, post=post)



@app.route("/show_questions/<int:test_id>",  methods=['GET', 'POST'])
@login_required
def show_questions(test_id):
	test = Test.query.get_or_404(test_id)
	question = TestQuestion.query.filter_by(test_id=test_id)
	if(len(question.all()) == 0):
		return redirect(url_for('new_test_question', test_id=test_id))


	else:
		print("Questions added already")

	flash('Your test is not empty! You can add more questions', 'success')
	return redirect(url_for('new_test_question', test_id=test_id))


@app.route("/take_test/<int:test_id>",  methods=['GET', 'POST'])
@login_required
def take_test(test_id):
	test = Test.query.get_or_404(test_id)
	question = TestQuestion.query.filter_by(test_id=test_id)
	q = (db.session.query(TestQuestion, Question)
    .filter(TestQuestion.test_id == test_id)
    .filter(TestQuestion.question_id == Question.id)
    .all())
	test.instructions = Markup(test.instructions)

	if(len(question.all()) == 0):
		return redirect(url_for('new_test_question', test_id=test_id))

	else:
		print("Questions ready to take the test")
		return render_template('new_tests.html', title="Taking Test", legend='Take test', test = test)

	flash('Your test is not empty! You can add more questions', 'success')
	return redirect(url_for('new_test_question', test_id=test_id))



@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		if form.picture.data:
			picture_file = save_post_picture(form.picture.data)
			post = Post(title=form.title.data, content=form.content.data, author=current_user, post_image_file=picture_file)
		else :
			post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.commit()
		flash("Your post has been updated !", "success")
		return redirect(url_for('post', post_id=post.id))
	elif request.method == 'GET':
		form.title.data = post.title
		form.content.data = post.content
	return render_template('create_post.html', title="Update Post", form=form, legend='Update Post')



@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('activity'))



@app.route("/main", methods=['GET'])
def mainTestFileUpload():
	return render_template('main.html')


@app.route("/upload", methods=["POST"])
def upload():
	uploaded_files = request.files.getlist("file[]")
	upload_pictures (uploaded_files)
	return ""


def upload_pictures(files):
	for x in files:
		save_album_picture(x)
	
	return ""

def save_album_picture(file):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(file.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/album_pics', picture_fn)
	file.save(picture_path)

	return picture_fn


@app.route('/rate_movie',methods=['GET','POST'])
def rate_movie():

    # Create cursor
    if request.method == 'POST':
    	data = request.get_json(force=True)
    	rating = data['rating']
    	id = data['id']
    	print(rating)
    	print(id)
    	flash('Movie Rated', 'success')
    	return redirect(url_for('mainTestFileUpload'))


@app.route("/alltests", methods=['GET'])
def all_tests():
	return render_template('new_tests.html')


@app.route("/teststests_bkp/", methods=['GET','POST'])
def tests_bkp():
        cur = mysql.connect().cursor()
        cur.execute('''SELECT json_object('question', question, 'a', a, 'b', b, 'c', c, 'd', d, 'ans', ans)
FROM questions;
''')
        rv = cur.fetchall()
        return jsonify(rv)

@app.route("/test_get_questions/", methods=['GET','POST'])
def test_get_questions():
	test_id = request.form['test_id']
	
	q = (db.session.query(TestQuestion, Question)
    .filter(TestQuestion.test_id == test_id)
    .filter(TestQuestion.question_id == Question.id)
    .all())

	empList = []
	choices = []
	for emp in q:
		choices.append(emp.Question.a);
		choices.append(emp.Question.b);
		choices.append(emp.Question.c);
		choices.append(emp.Question.d);
		
		empDict = {
		'question': emp.Question.question_content,
		'choices' : choices,
		'positive_marks' : emp.Question.positive_marks,
		'negative_marks' : emp.Question.negative_marks,
		'section' : emp.Question.section
		}
		choices = []
		empList.append(empDict)
	return json.dumps(empList)




@app.route("/test_get_answers/", methods=['GET','POST'])
def test_get_answers():
	test_id = request.form['test_id']
	
	q = (db.session.query(TestQuestion, Question)
    .filter(TestQuestion.test_id == test_id)
    .filter(TestQuestion.question_id == Question.id)
    .all())
	empList = []
	for emp in q:		
		empDict = {
		'correctAnswer': emp.Question.ans,
		'positive_marks' : emp.Question.positive_marks,
		'negative_marks' : emp.Question.negative_marks
		}
		empList.append(empDict)
	return json.dumps(empList)


@app.route("/test_update_user_score/", methods=['GET','POST'])
def test_update_user_score():
	test_id = request.form['test_id']
	user_id = request.form['user_id']
	user_score = request.form['user_score']
	positive_score = request.form['positive_score']
	negative_score = request.form['negative_score']
	correct_answers = request.form['correct_answers']
	wrong_answers = request.form['wrong_answers']
	no_answers = request.form['no_answers']
	attempted_ques = request.form['no_of_attempted_ans_ques']
	
	usertest = UserTest(test_id=test_id, user_id=user_id,user_score=user_score, positive_score=positive_score,negative_score=negative_score, correct_answers=correct_answers,wrong_answers=wrong_answers,no_answers=no_answers, attempted_ques=attempted_ques )
	db.session.add(usertest)
	db.session.commit()

	return "Succesfully updated user score"




