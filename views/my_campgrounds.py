from flask.views import MethodView
from flask import render_template, session, redirect, url_for
from model.campground import Campground


class MyCampgrounds(MethodView):
    def get(self):
        session['home'] = False;
        if session.get('id') is None:
            return redirect(url_for('login'))
        campgrounds=Campground.query.order_by(Campground.id.desc()).filter_by(user_id=session.get('id'));
        count=campgrounds.count();
        return render_template("my-campgrounds.html",campgrounds=campgrounds,count=count);
