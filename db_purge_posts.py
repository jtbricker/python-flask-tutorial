#!flask/Scripts/python

"""
This script deletes all posts from the db
"""
from app.models import Post
from app import db
for post in Post.query.all():
    db.session.delete(post)
db.session.commit()