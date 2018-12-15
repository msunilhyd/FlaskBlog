from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MY_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format('kumaruser', 'kumar', 'localhost', 3306, 'kumardb')
app.config['MYSQL_DATABASE_USER'] = 'kumaruser';
app.config['MYSQL_DATABASE_PASSWORD'] = 'kumar';
app.config['MYSQL_DATABASE_DB'] = 'kumardb';
app.config['MYSQL_DATABASE_HOST'] = 'localhost';



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager =  LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mysql = MySQL(app)


from flaskBlog.models import User, Post


db.create_all()
db.session.commit()



from flaskBlog import routes



