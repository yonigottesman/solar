from app import db


class Body(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    horizon_id = db.Column(db.Integer)
    wiki = db.Column(db.String(64))
    deltas = db.relationship('Delta', backref='body', lazy='dynamic')

    def __repr__(self):
        return '<Body {}>'.format(self.name)


class Delta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, index=True)
    au = db.Column(db.Float)
    body_id = db.Column(db.Integer, db.ForeignKey('body.id'))

    def __repr__(self):
        return '<delta {} {} {}>'.format(self.body_id, self.time, self.au)
