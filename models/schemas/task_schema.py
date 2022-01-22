from flask_marshmallow import Schema

class Task_Schema(Schema):
    class Meta:
        fields = ("task_id", "title", "description")


task_schema = Task_Schema()
tasks_schema = Task_Schema(many=True)
