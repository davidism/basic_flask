from sqlalchemy.sql import expression
from basic_app import db


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True, index=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(254), nullable=False, unique=True, index=True)
    password = db.Column(db.String(60))
    name = db.Column(db.String(254), nullable=False, default="", server_default="")
    email = db.Column(db.String(254), nullable=False, default="", server_default="")
    active = db.Column(db.Boolean, nullable=False, default=False, server_default=expression.true())

    groups = db.relationship(Group, lambda: user_group, backref=db.backref("users"))

user_group = db.Table("user_group",
    db.Column("user_id", db.Integer, db.ForeignKey(User.id), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey(Group.id), primary_key=True)
)
