import sqlalchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    votes = db.Column(db.Integer, nullable=True)
    video_path = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)
    fb_id = db.Column(db.String(255), unique=True, nullable=True)
    g_id = db.Column(db.String(255), unique=True, nullable=True)
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, username, email, name, surname, fb_id, g_id):
        self.username = username
        self.email = email
        self.name = name
        self.surname = surname
        self.fb_id = fb_id
        self.g_id = g_id

    def __repr__(self):
        return f"{self.id}"
