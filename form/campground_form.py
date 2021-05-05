from wtforms import StringField, FloatField, TextAreaField,validators
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from flask_wtf.file import FileField,FileRequired,FileAllowed
class CreateCampground(FlaskForm):
    title = StringField("Campground title:",validators=[InputRequired()])
    city = StringField("City", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    price = FloatField("Minimum price",validators=[InputRequired()])
    image = FileField('Campground image', validators=[
        FileAllowed(['jpg', 'png','jpeg'], 'Images only!')
    ])
    description = TextAreaField("Description", validators=[InputRequired()])