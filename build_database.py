import os
from config import db
from models import User, Post

# Data to initialize database with
POST = [
    {"title": "Sagrado Futebol", "post_user_id": "0", "votes": "0", "video_path": "/", "isPublished": "True"}
]

# Delete database file if it exists currently
if os.path.exists("sagrado.db"):
    os.remove("sagrado.db")

# Create the database
db.create_all()

# iterate over the POST structure and populate the database
for post in POST:
    p = Post(title=post.get("title"), 
    #pub_date=post.get("pub_date"), 
    post_user_id=post.get("post_user_id"), 
    votes=post.get("votes"),
    video_path=post.get("video_path")
    )
    db.session.add(p)

db.session.commit()