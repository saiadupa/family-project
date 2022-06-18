
from flask import Blueprint, render_template, session, redirect, url_for
from functools import wraps
from ..models import Users

user = Blueprint('user', __name__ , static_folder="static", template_folder="templates")

def is_user_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'email' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('hom.login'))
    return wrap


@user.route('/')
@is_user_in
def home():
    email = session['email']
    user = Users.query.filter_by(email=email).first()
    return render_template('user/user.html', user = user)

@user.route('/about')
@is_user_in
def about():
    email = session['email']
    return render_template('about.html', email=email, user = True)

@user.route('/contact', methods=['GET','POST'])
@is_user_in
def contact():
    email = session['email']
    return render_template('contact.html', email=email, user = True)


@user.route('/logout')
@is_user_in
def logout():
    email = session['email']
    session.pop('email', None)
    return redirect(url_for('hom.home'))

