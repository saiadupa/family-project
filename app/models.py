from . import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sur_name = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    