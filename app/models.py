from app import *

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True,primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def is_active(self):
       return True
    
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True,primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def is_active(self):
       return True

class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True,nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(255))
    datetime = db.Column(db.DateTime)