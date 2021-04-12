from flask.views import MethodView
from flask import render_template, session
from model.campground import Campground


class Index(MethodView):
    def get(self):
        campgrounds=Campground.query.order_by(Campground.id.desc()).all();
        session['home']=True;
        return render_template("index.html",campgrounds=campgrounds);
