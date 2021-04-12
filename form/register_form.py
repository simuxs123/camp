from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Email
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField

class RegisterForm(FlaskForm):
    first_name=StringField("First name",
                           validators=[DataRequired()])
    last_name = StringField("Last name",
                             validators=[DataRequired()])
    email = EmailField("Email",
                       validators=[DataRequired(), Email()])
    password=PasswordField("Password",
                           validators=[DataRequired()])