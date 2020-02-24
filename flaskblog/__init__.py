from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='c7397ed99b2395510fc601dd0ca27f53'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


db = SQLAlchemy(app)
from flaskblog import routes
