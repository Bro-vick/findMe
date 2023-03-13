from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class EditProfileForm(FlaskForm):
    name = StringField('Full name', validators=[Length(0, 100)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    email = StringField('Email Address')
    facebook = StringField('Facebook URL')
    linkedin = StringField('Linkedin URL')
    twitter = StringField('Twitter URL')
    github = StringField('Github URL')
    youtube = StringField('Youtube Channel URL')
    instagram = StringField('Instagram URL')
    snapchat = StringField('Snapchat  URL')
    tiktok = StringField('TikTok URL')
    medium = StringField('Medium URL')
    submit = SubmitField('Submit')

class UploadPicture(FlaskForm):
    profile_picture = FileField('Profile picture', validators=[DataRequired()])
    submit = SubmitField('Submit')

"""
class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
        """
