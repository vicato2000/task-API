from flask_marshmallow import Schema

class Tag_Schema(Schema):
    class Meta:
        fields = ('tag_id','user_id','tag_name')

tag_schema = Tag_Schema()
tags_schema = Tag_Schema(many=True)