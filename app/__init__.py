from flask import Flask
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    from .views import main, chat
    app.register_blueprint(main.bp)
    app.register_blueprint(chat.bp)

    return app
