from utils.db import db

users = db.table(
    "users",
    db.Column("user_id", db.Integer, db.ForeignKey("user.user_id") , primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("group.group_id"), primary_key=True)
)

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(10), nullable=True)
    #user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=True)
    users = db.relationship("Users", secondary=users, lazy="dynamic", backref=db.backref("group", lazy='dynamic'))

    def __init__(self, users, user_id, group_name):
        #self.users = users
        #self.user_id = user_id
        self.group_name = group_name