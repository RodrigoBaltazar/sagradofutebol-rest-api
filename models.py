from datetime import datetime
from config import db, ma

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    #pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    votes = db.Column(db.Integer, nullable=True)
    video_path = db.Column(db.String(255), unique=True, nullable=True)
    #timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        include_relationships = True
        load_instance = True
        
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)
    fb_id = db.Column(db.String(255), unique=True, nullable=True)
    g_id = db.Column(db.String(255), unique=True, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True