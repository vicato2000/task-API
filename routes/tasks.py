from flask import Blueprint, request

from models.schemas.task_schema import task_schema
from models.task import Task
from utils.db import db

tasks = Blueprint("tasks", __name__)


@tasks.route("/new", methods=["POST"])
def create_task():
    title = request.json.get("title")
    description = request.json.get("description")

    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)
