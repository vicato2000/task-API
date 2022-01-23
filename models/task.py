from utils.db import db
from models.user import User


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship(User)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id
