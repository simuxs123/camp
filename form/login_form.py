from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Email
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
class LoginForm(FlaskForm):
    email=EmailField("Email",
                         validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"}
                         )
    password=PasswordField("Password",
                           validators=[DataRequired()],render_kw={"placeholder": "Password"})