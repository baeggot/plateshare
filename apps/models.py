__author__ = 'sol'

from apps import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    contents = db.relationship('Content', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.email)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    created_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Content %r>' % (self.title)


