import os

import tinify
from flask.views import MethodView
from flask import render_template, session, redirect, url_for,request
from werkzeug.datastructures import CombinedMultiDict, FileStorage
from werkzeug.utils import secure_filename
from model.user import User
from model.campground import Campground
from form.campground_form import CreateCampground
from model import db


class Update(MethodView):
    def get(self,campground_id):
        if session.get('id') is None:
            return redirect(url_for('login'))
        camp = Campground.query.filter_by(id=campground_id,user_id=session.get('id'))
        if camp.count()==0:
            return redirect(url_for('index'))
        if session.get('id') != camp.one().user_id:
            return redirect(url_for('index'))
        campground_form = CreateCampground(obj=camp.one());
        return render_template('add-campground.html', campground_form=campground_form,button='Update campground')
    def post(self,campground_id):
        camp = Campground.query.filter_by(id=campground_id, user_id=session.get('id')).one();
        campground_form = CreateCampground(obj=camp)
        if campground_form.validate_on_submit():
            user = User.query.filter_by(id=session.get('id')).first()

            file = campground_form.image.data
            if type(file) != str:
                os.remove(os.path.join('static/img', camp.image))
                image_file = secure_filename(user.first_name+'_'+file.filename)
                tinify.key = 'LQQVx8qmRrXNr0cV410NK4YgwDd7ZGpN'
                tinify.from_file(path=file).to_file(os.path.join('static/img', image_file))
            else:
                image_file=camp.image;
            campground_form.populate_obj(camp)
            camp.image = image_file
            db.session.commit()
            return redirect(url_for('campground',
                                    campground_id=campground_id))
        else:
            return render_template('add-campground.html', campground_form=campground_form)