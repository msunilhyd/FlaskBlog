from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskext.mysql import MySQL
from flask_json import FlaskJSON, JsonError, json_response

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MY_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format('kumaruser', 'kumar', 'localhost', 3306, 'kumardb')
app.config['MYSQL_DATABASE_USER'] = 'kumaruser';
app.config['MYSQL_DATABASE_PASSWORD'] = 'kumar';
app.config['MYSQL_DATABASE_DB'] = 'kumardb';
app.config['MYSQL_DATABASE_HOST'] = 'localhost';

app.config['JSON_ADD_STATUS'] = False
app.config['JSON_DATETIME_FORMAT'] = '%d/%m/%Y %H:%M:%S'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager =  LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mysql = MySQL(app)
json = FlaskJSON(app)



from flaskBlog.models import User, Post


db.create_all()
db.session.commit()



from flaskBlog import routes



