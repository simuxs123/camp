from flask import Flask
from model import db
from views.index import Index;
from views.login import Login;
from views.register import Register;
from views.logout import Logout;
from views.add_campground import AddCampground;
from views.campground_details import CampgroundDetails
from views.my_campgrounds import MyCampgrounds
from views.delete import Delete
from views.update import Update
from config import Config;
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all(app=app)

app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/register', view_func=Register.as_view('register'))
app.add_url_rule('/add-campground', view_func=AddCampground.as_view('add-campground'))
app.add_url_rule('/my-campgrounds', view_func=MyCampgrounds.as_view('my-campgrounds'))
app.add_url_rule('/campground/<int:campground_id>', view_func=CampgroundDetails.as_view('campground'))
app.add_url_rule('/logout', view_func=Logout.as_view('logout'))
app.add_url_rule('/campground/<int:campground_id>/delete', view_func=Delete.as_view('delete'))
app.add_url_rule('/campground/<int:campground_id>/update', view_func=Update.as_view('update'))


if __name__ == '__main__':
    app.run()
