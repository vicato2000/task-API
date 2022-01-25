from flask import Blueprint, request
from models.group import Group
from utils.db import db
from models.schemas.group_schema import group_schema, groups_schema

groups = Blueprint('groups',__name__)

@groups.route('/api/groups/new', methods=['POST'])
def create_group():
    group_name = request.json.get('group_name')

    new_group = Group(group_name)
    db.session.add(new_group)
    db.session.commit()

    return group_schema.jsonify(new_group)