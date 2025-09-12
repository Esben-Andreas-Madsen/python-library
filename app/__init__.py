from flask import Flask
from extentions import db
from routes import register_routes

def create_app(config_class=None):
    app = Flask(__name__)
    
    if config_class:
        app.config.from_object(config_class)
    
    db.init_app(app)
    
    register_routes(app)
    
    return app
