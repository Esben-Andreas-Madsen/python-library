from flask import Flask
from .extensions import db
from app.routes.routes import routes

def create_app(config_class=None):
    app = Flask(__name__)
    
    if config_class:
        app.config.from_object(config_class)
    
    db.init_app(app)
    
    app.register_blueprint(routes)
    
    return app

def init_db(app):
    with app.app_context():
        db.create_all()
        print("Database initialized!")