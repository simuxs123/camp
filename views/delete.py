from flask import redirect, url_for, session
import os
from flask.views import MethodView
from model import db
from model.campground import Campground

class Delete(MethodView):
    def get(self,campground_id):
        camp = Campground.query.filter_by(id=campground_id).one()
        if session.get('id') != camp.user_id:
            return redirect(url_for('index'))
        os.remove(os.path.join('static/img', camp.image))
        db.session.delete(camp)
        db.session.commit()
        return redirect(url_for('my-campgrounds'))