
import os
from flask import Flask , jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the db

db = SQLAlchemy()

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)
    
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    #app.config['SQLALCHEMY_DATABASE_URI'] = "mysql:////db/Database/users_dev.db"

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprints
    app.register_blueprint(users_blueprints)

    # shell context for flask cli
    app.shell_context_processor({'app':app , 'db':db})
    return app