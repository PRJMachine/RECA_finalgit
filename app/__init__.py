from flask import Flask
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    from .views import main
    app.register_blueprint(main.bp)

    return app
