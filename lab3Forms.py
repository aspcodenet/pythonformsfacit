from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, ValidationError
from wtforms.fields import IntegerField, SelectField, RadioField


def emailContains(form, field):
    if not field.data.endswith('systementor.se'):
        raise ValidationError('Invalid email domain')

class Lab3Form(FlaskForm):
    fname = StringField('fname', validators=[validators.DataRequired()])
    lname = StringField('lname', validators=[validators.DataRequired()])
    email = StringField('email', validators=[validators.DataRequired(), emailContains])
    pword = PasswordField('pword', validators=[validators.DataRequired()])
    cpword = PasswordField('cpword', validators=[validators.DataRequired()])
    country = SelectField('country', choices=[('se','Sweden'),('no', 'Norway'),('dk','Denmark')] )
    utype = SelectField('utype', choices=[('norm','Normal'),('prem', 'Premium'),('bip','BIP')] )
