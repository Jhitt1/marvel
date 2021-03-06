from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login, app

class User(UserMixin, db.Model): # working table for user registration
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Hero(UserMixin, db.Model): # table now works, but the foreignkey syntax is throwing errors every time I try to use it.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(255))
    comics_appeared = db.Column(db.Integer, index=True)
    super_power = db.Column(db.String(55), index=True)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #this line is not functional because I am stuck trying to validate user log in
