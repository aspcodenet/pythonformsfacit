from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, ValidationError
from wtforms.fields import IntegerField, TelField, EmailField,RadioField, SelectField, SelectMultipleField




class Lab4Form(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired()])
    mob = TelField('mob', validators=[validators.DataRequired()])
    address = StringField('address', validators=[validators.DataRequired()])
    post = StringField('post', validators=[validators.DataRequired()])
    port = StringField('port', validators=[validators.DataRequired()])
    email = EmailField('email', validators=[validators.DataRequired()])
    edu = SelectMultipleField('edu', choices=[('hsk','Högskoleutbildning'),('ysk', 'Yrkeshögskola'),('gym','Gymnasial utbildning')] )
    work = RadioField('work',choices=[('se','Kan arbeta inom Sverige'),('eu', 'Kan arbeta inom EU'),('reg','Endast arbeta regionalt')] )
    lic = BooleanField('lic' )
    car = BooleanField('car' )

