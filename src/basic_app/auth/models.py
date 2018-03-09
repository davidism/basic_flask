from sqlalchemy.sql import expression
from basic_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(60))
    email = db.Column(db.String(254), nullable=False, default="", server_default="")
    active = db.Column(db.Boolean, nullable=False, default=False, server_default=expression.true())
