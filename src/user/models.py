from datetime import datetime

from core import db


class User(db.Model):
    id = db.Column(db.BigInteger().with_variant(db.Integer, 'sqlite'), unique=True, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"
