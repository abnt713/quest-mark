__author__ = 'alisonbnt'

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128))
    adventurer = db.relationship("Adventurer", uselist=False, backref="adventurer")

class Adventurer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(48))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    bio = db.Column(db.Text)



