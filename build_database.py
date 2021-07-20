from config import db
from models import User, Post

# Data to initialize database with
POST = [
    {"id": "0", "title": "Sagrado Futebol", "votes": "0", "video_path": "/"},
    {"id": "1", "title": "Internaticionale", "votes": "10", "video_path": "/123"},
    {"id": "2", "title": "Internaticionale", "votes": "10", "video_path": "/1232"}
]


# Create the database
db.create_all()

# iterate over the POST structure and populate the database
for post in POST:
    p = Post(title=post.get("title"), 
    #pub_date=post.get("pub_date"), 
    #post_user_id=post.get("post_user_id"), 
    votes=post.get("votes"),
    video_path=post.get("video_path")
    )
    db.session.add(p)

db.session.commit()