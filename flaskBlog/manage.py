from flaskBlog import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)


manager = Manager(app)


manager.add_command('db', MigrateCommand)

from flaskBlog.models import User, Post, Test, Question, TestQuestion, UserTest


if __name__ == '__main__':
	manager.run()