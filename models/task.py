from utils.db import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description
