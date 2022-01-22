from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import true

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://admin:admin@localhost/task'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(10),unique=True)
    description = db.Column(db.String(100))

    def __init__(self,title,description):
        self.title = title
        self.description = description

db.create_all()

class Task_Schema(ma.Schema):
    class Meta:
        fields = ('task_id','title','description')

task_schema = Task_Schema()
tasks_schema = Task_Schema(many=True)



# Endpoints

@app.route('/task',methods=['POST'])
def create_task():
    title = request.json.get('title')
    description = request.json.get('description')

    new_task = Task(title,description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)
    

# Execute

if __name__ == "__main__":
    app.run(debug = True)
