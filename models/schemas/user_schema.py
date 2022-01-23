from flask_marshmallow import Schema


class User_Schema(Schema):
    class Meta:
        fields = ('user_id', 'username', 'email', 'password')


user_schema = User_Schema()
users_schema = User_Schema(many=True)
