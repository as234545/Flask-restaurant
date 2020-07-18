from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import sys
from datetime import datetime, timedelta
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
app = Flask(__name__)

def create_app():


    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db10.db'
    app.app_context().push()
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    return app

 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


    def __init__(self, email, password, name ):
        self.email = email
        self.password = password
        self.name = name

        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Resturants(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    def __init__(self, name, date_posted, content ):
        self.name = name
        self.date_posted = datetime.now()
        self.content = content



class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guestnum = db.Column(db.Integer,nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    menutype = db.Column(db.Text, nullable=False) #future update: add predefined option
    notes = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=True)

    def __init__(self, guestnum, date, menutype, notes , user_id):
        self.guestnum = guestnum
        self.date = date
        self.menutype = menutype
        self.notes = notes
        self.user_id = user_id


db.create_all(app=create_app())