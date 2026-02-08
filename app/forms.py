from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
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
