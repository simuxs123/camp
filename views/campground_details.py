from flask.views import MethodView
from flask import render_template, session, request
from model import db
from model.user import User
from model.campground import Campground


class CampgroundDetails(MethodView):
    def get(self,campground_id):
        camp = Campground.query.filter_by(id=campground_id).one()
        return render_template("campground-details.html",campground=camp,campground_id=campground_id,home=session['home']);
