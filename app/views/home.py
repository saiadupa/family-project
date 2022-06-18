from flask import Blueprint, redirect, render_template, request, url_for, jsonify, session
from passlib.hash import sha256_crypt
from ..models import *

hom = Blueprint('hom', __name__ , static_folder="static", template_folder="templates")

@hom.route('/')
def home():
    return render_template('home/home.html')

@hom.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        pswd = request.form.get('pswd')

        user = Users.query.filter_by(email=email).first()

        if user:
            if sha256_crypt.verify(pswd, user.password):
                session['email'] = user.email
                return redirect(url_for('user.home'))
    return render_template('home/login.html')

@hom.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        s_name = request.form.get('s_name')
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        email = request.form.get('email')
        pswd = request.form.get('pswd')

        pswd = sha256_crypt.hash(pswd)
        
        if Users.query.filter_by(email=email).first():
            return jsonify({"message": "This email is already registered."})
        else:
            user = Users(sur_name=s_name,first_name=f_name,last_name=l_name,email=email,password=pswd)
            db.session.add(user)
            db.session.commit()

            session['email'] = email

            return redirect(url_for('user.home'))

    return render_template('home/signup.html')

@hom.route('/about')
def about():
    return render_template('about.html')

@hom.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')


