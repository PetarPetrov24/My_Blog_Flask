from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=100)])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Publish')

class UpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3)])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Update Post')

class PostDelete(FlaskForm):
    submit = SubmitField('Delete Post')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
