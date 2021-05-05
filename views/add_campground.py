import os
import tinify
from flask.views import MethodView
from flask import render_template, session, redirect, url_for
from werkzeug.utils import secure_filename

from model.campground import Campground
from model.user import User;
from form.campground_form import CreateCampground
from model import db


class AddCampground(MethodView):
    def get(self):
        campground_form = CreateCampground();
        session['home'] = False;
        if session.get('id') is None:
            return redirect(url_for('login'))
        return render_template('add-campground.html', campground_form=campground_form,button='Add campground')
    def post(self):
        campground_form = CreateCampground()
        if campground_form.validate_on_submit():
            user = User.query.filter_by(id=session.get('id')).first()
            file = campground_form.image.data
            if file:
                image_file = secure_filename(user.first_name+'_'+file.filename)
                tinify.key = 'LQQVx8qmRrXNr0cV410NK4YgwDd7ZGpN'
                tinify.from_file(path=file).to_file(os.path.join('static/img', image_file))
            else:
                image_file=""


            new_campground = Campground(title=campground_form.title.data,
                                  city=campground_form.city.data,
                                  address=campground_form.address.data,
                                  price=campground_form.price.data,
                                  image=image_file,
                                  description=campground_form.description.data,
                                  user_id=user.id)
            db.session.add(new_campground)
            db.session.commit()
            return redirect(url_for('campground',
                                    campground_id=Campground.query.order_by(Campground.id.desc()).first().id))
        else:
            return render_template('add-campground.html', campground_form=campground_form)