from flask_marshmallow import Schema

class Group_Schema(Schema):
    class Meta:
        fields = ('group_id', 'group_name')

group_schema = Group_Schema()
groups_schema = Group_Schema(many=True)