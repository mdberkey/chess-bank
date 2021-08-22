import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

project_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(project_dir, 'chess_database.db')
database_file = f'sqlite:///{db_dir}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = 'You must be logged in to access this page.'
login_manager.login_view = 'auth.login'
