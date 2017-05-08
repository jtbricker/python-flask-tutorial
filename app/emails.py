'''
This module defines email behaviors
'''
from flask import render_template
from config import ADMINS
from flask_mail import Message
from app import mail, app
from .decorators import async

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    '''
    Sends an email
    Inputs:
        followed:  The user being followed
        follower: The user following the followed user
    '''
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

def follower_notification(followed, follower):
    '''
    Sends an email notifying a user when they are followed by another user
    Inputs:
        followed:  The user being followed
        follower: The user following the followed user
    '''
    send_email("[microblog] %s is now following you!" % follower.nickname,
               ADMINS[0],
               [followed.email],
               render_template("follower_email.txt",
                               user=followed, follower=follower),
               render_template("follower_email.html",
                               user=followed, follower=follower))
