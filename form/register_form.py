from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Email
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField

class RegisterForm(FlaskForm):
    first_name=StringField("First name",
                           validators=[DataRequired()],render_kw={"placeholder": "First name"})
    last_name = StringField("Last name",
                             validators=[DataRequired()],render_kw={"placeholder": "Last name"})
    email = EmailField("Email",
                       validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    password=PasswordField("Password",
                           validators=[DataRequired()],render_kw={"placeholder": "Password"})