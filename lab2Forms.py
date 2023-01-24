from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, TextAreaField, PasswordField, validators, ValidationError
from wtforms.fields import IntegerField, EmailField



class Lab2Form(FlaskForm):
    email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    message = TextAreaField('message', validators=[validators.InputRequired("Not including a message would be stupid")])
