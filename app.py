from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.tasks import tasks
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb+pymysql://admin:admin@localhost/taskdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)
Marshmallow(app)


# Configure endpoint
app.register_blueprint(tasks)

