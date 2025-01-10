from flask import Flask
from .api import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.ProductionConfig')  # Load production configuration
    app.register_blueprint(api, url_prefix='/')
    return app
