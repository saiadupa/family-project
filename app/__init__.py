from flask import Flask, render_template, session, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

from .models import *

db.create_all(app=app)

from .views import home,user

app.register_blueprint(home.hom, url_prefix="/")
app.register_blueprint(user.user, url_prefix="/user")



   

