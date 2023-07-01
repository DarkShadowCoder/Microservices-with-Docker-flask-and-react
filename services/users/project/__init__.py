import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app

app = Flask(__name__)

# Set config
app.config.from_object('project.config.DevelopmentConfig')
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

#model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.String(128),nullable=False)
    email = db.Column(db.String(128),nullable=False)
    active = db.Column(db.Boolean, default=True , nullable=False)

    def __init__(self, username , email):
        self.username = username
        self.email = email

#routes
@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message':'pong!',
    })


if __name__=='__main__':
    app.run(debug=True)