from wtforms import StringField, FloatField, TextAreaField,validators
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from flask_wtf.file import FileField,FileRequired,FileAllowed
class CreateCampground(FlaskForm):
    title = StringField("Campground title:",validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    price = FloatField("Minimum price",validators=[InputRequired()])
    image = FileField('Campground image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png','jpeg'], 'Images only!')
    ])
    description = TextAreaField("Description", validators=[InputRequired()])