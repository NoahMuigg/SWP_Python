from flask import Flask
from .Server import Server

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hallo'
    
    app.register_blueprint(Server, url_prefix="/")

    return app