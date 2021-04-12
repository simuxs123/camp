from model import db
from model.user import User
from form.login_form import LoginForm
from flask import render_template,redirect,url_for,session
from werkzeug.security import check_password_hash
from flask.views import MethodView

class Login(MethodView):
    def get(self):
        if session.get('id'):
            return redirect(url_for('index'))
        login_form=LoginForm()
        return render_template('login.html',login_form=login_form)
    def post(self):
        login_form=LoginForm()
        if login_form.validate_on_submit():
            user=User.query.filter_by(email=login_form.email.data).first()
            if user is None:
                login_form.email.data = ""
                return render_template('login.html', login_form=login_form,error="Email doesnt exist")
                # return redirect (url_for('login'))
            elif check_password_hash(user.password,login_form.password.data):
                session['id']=user.id
                return redirect(url_for('index'))
            else:
                return render_template('login.html', login_form=login_form, error="Incorrect password")
                # return redirect(url_for('login'))