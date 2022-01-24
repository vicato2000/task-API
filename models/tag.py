from utils.db import db


class Tag(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    tag_name = db.Column(db.String(10), nullable=False)
    tasks = db.relationship("Task", backref="_tag", lazy=True)

    def __init__(self, user_id, tag_name):
        self.user_id = user_id
        self.tag_name = tag_name
