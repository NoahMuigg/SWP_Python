from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hallo'
    from .Server import Server
    app.register_blueprint(Server, url_prefix="/")

    return app