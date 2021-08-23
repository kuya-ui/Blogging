from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    title_blogging = StringField('Title')
    description = TextAreaField('Write a Description', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Comment')


class SubscriberForm(FlaskForm):
    email = StringField('Your Email Address')
    name = StringField('Enter your name',validators = [Required()])
    submit = SubmitField('Subscribe')