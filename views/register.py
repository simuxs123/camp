from flask import render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash
from flask.views import MethodView
from model import db
from model.user import User
from form.register_form import RegisterForm

class Register(MethodView):
    def get(self):
        if session.get('id'):
            return redirect(url_for('index'))
        registration_form=RegisterForm();
        return render_template('register.html',title="Registration",registration_form=registration_form,session=session.get('id'))
    def post(self):
        registration_form=RegisterForm()
        if registration_form.validate_on_submit():
            user = User.query.filter_by(email=registration_form.email.data).first()
            if user :
                registration_form.email.data = ""
                return render_template('register.html', registration_form=registration_form, error="Email already exist")
            new_user=User(first_name=registration_form.first_name.data,
                          last_name=registration_form.last_name.data,
                          email=registration_form.email.data,
                          password=generate_password_hash(registration_form.password.data),
                          )
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering')
            return redirect((url_for('login')))
        return render_template('register.html',title="Registration",registration_form=registration_form,session=session.get('id'))
