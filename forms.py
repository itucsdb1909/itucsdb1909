from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms import validators, Form

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=50)])
    email = StringField('Email Address', [validators.Length(min=0, max=50)])
    name = StringField('Name', [validators.Length(min=0, max=50)])
    surname = StringField('Surname', [validators.Length(min=0, max=50)])
    age = StringField('Age', [validators.Length(min=0, max=3)])
    gender = StringField('Gender', [validators.Length(min=0, max=5)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

# POEM OPERATIONS
class PoemAddForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=4)])
    year = StringField('Year', [validators.Length(min=0, max=50)])
    content = StringField('Content', [validators.Length(min=0, max=50)])
    author = StringField('Author', [validators.Length(min=0, max=50)])
    category = StringField('Category', [validators.Length(min=0, max=50)])

class PoemUpdateForm(Form):
    id = StringField('Id of The Poem', [validators.Length(min=1, max=4)])
    title = StringField('Title', [validators.Length(min=0, max=50)])
    year = StringField('Year', [validators.Length(min=0, max=50)])
    content = StringField('Content', [validators.Length(min=0, max=50)])
    author = StringField('Author', [validators.Length(min=0, max=50)])
    category = StringField('Category', [validators.Length(min=0, max=50)])

class PoemDeleteForm(Form):
    Poem_id = StringField('Id', [validators.Length(min=1, max=5)])

#BOOK OPERATIONS
class BookAddForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=4)])
    category = StringField('Category', [validators.Length(min=0, max=50)])
    number_of_pages = StringField('Number of pages', [validators.Length(min=0, max=4)])
    publisher = StringField('Publisher', [validators.Length(min=0, max=50)])
    author = StringField('Author', [validators.Length(min=0, max=50)])

class BookUpdateForm(Form):
    id = StringField('Id of The Book', [validators.Length(min=1, max=4)])
    name = StringField('Name', [validators.Length(min=0, max=50)])
    category = StringField('Category', [validators.Length(min=0, max=50)])
    number_of_pages = StringField('Number of pages', [validators.Length(min=0, max=4)])
    publisher = StringField('Publisher', [validators.Length(min=0, max=50)])
    author = StringField('Author', [validators.Length(min=0, max=50)])

class BookDeleteForm(Form):
    Book_id = StringField('Id', [validators.Length(min=1, max=4)])
