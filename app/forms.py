'''
Defines Forms created using FlaskForms
'''
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length
from app.models import User


class LoginForm(FlaskForm):
    '''
    Custom Form for Logging in Users
    '''
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class EditForm(FlaskForm):
    '''
    Custom Form for Editing User Profile
    '''
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        '''
        This method overrides FlaskFOrm's validate method, calls it first and
        then calls custom validations to make sure the nickname is not already
        in use
        '''
        if not FlaskForm.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. \
                 Please choose another one.')
            return False
        return True
