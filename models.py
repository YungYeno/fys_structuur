from __init__ import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    flightnumber = db.Column(db.String(100))
    seatnumber = db.Column(db.String(100))