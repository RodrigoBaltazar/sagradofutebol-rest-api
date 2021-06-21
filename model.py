from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sf:sf@localhost/sagradofutebol'
pymysql.install_as_MySQLdb()

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)
    fb_id = db.Column(db.String(255), unique=True, nullable=True)
    g_id = db.Column(db.String(255), unique=True, nullable=True)
    
    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    votes = db.Column(db.Integer, nullable=True)
    video_path = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title

db.create_all()