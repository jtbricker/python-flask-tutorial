"""
This module defines the models for our database
"""
from hashlib import md5
from app import db

followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    """
    This class represents a user of our app
    """
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    followed = db.relationship('User',
                               secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')

    def follow(self, user):
        '''
        Add the given user to this user's list of followed users
        '''
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        '''
        Remove the given user from this user's list of followed users
        '''
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        '''
        Returns true if the given user is in this user's list of followed users
        '''
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        '''
        Returns the list of posts made by followed users
        '''
        return Post.query.join(followers, (followers.c.followed_id == Post.user_id)) \
            .filter(followers.c.follower_id == self.id).order_by(Post.timestamp.desc())

    @property
    def is_authenticated(self):
        '''
        Should just return True unless the object represents a user that should not be
        allowed to authenticate for some reason.
        '''
        return True

    @property
    def is_active(self):
        '''
        Should return True for users unless they are inactive, for example because they
        have been banned.
        '''
        return True

    @property
    def is_anonymous(self):
        '''
        Should return True only for fake users that are not supposed to log in to the system.
        '''
        return False

    @staticmethod
    def make_unique_nickname(nickname):
        '''
        Given a nickname, check if it is taken in the db and
        iterate versions of the nickname until it is unique
        '''
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            version += 1
        return new_nickname

    def get_id(self):
        '''
        Return the id of the user
        '''
        try:
            return unicode(self.id) #python2
        except NameError:
            return str(self.id) #python3

    def avatar(self, size):
        '''
        Get avatar from gravatar using user's email address
        '''
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' \
            % (md5(self.email.encode('utf-8')).hexdigest(), size)

    def __repr__(self):
        return '<User %r>' %(self.nickname)

class Post(db.Model):
    """
    This class represents a post made by a user of our app
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' %(self.body)
