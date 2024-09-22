from flask import Flask
#Import database ORM
from flask_sqlalchemy import SQLAlchemy
#Import SQLAlchemy utilities and exception handlers
from sqlalchemy_utils import database_exists
from sqlalchemy import func,exc
#Import Redis
from flask_redis import FlaskRedis

import os
#Sets environment variables from .env


db = SQLAlchemy()
r = FlaskRedis()

def init_app():
    """Initialize the core applications."""
    app = Flask(__name__,instance_relative_config=False)
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')
    

    #Initialize Plugins
    db.init_app(app)
    r.init_app(app)

    with app.app_context():
        
        from .settings import bp as settings_blueprint
        from .game import bp as games_blueprint

        db.create_all()
        app.register_blueprint(settings_blueprint)
        app.register_blueprint(games_blueprint)

        print(app.config)
        return app
    