from project import db
from datetime import datetime



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable = False)
    permissions = db.Column(db.String(20), nullable = False , default = 'user' )

    def __repr__(self):
        return "User " + str(self.username) + "permissions" + str(self.permissions)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image_file= db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    author = db.Column(db.String(20), nullable=False, default = 'Admin')
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return "Post id " + str(self.id)