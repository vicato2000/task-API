from flask import Blueprint, request
from models.user import User
from utils.db import db
from models.schemas.user_schema import user_schema, users_schema

users = Blueprint("users", __name__)


@users.route("/api/users/new", methods=["POST"])
def create_user():
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    new_user = User(username, email, password)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

