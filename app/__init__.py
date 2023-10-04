from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


# app = Flask(__name__)
# @app.route('/', methods=['GET'])
# def hello_world():
#     return 'Hello, World! This is your API.'
#     render_template("home.html")


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    
    # 블루프린트
    from .views import main, chat, auth_views
    app.register_blueprint(main.bp)
    app.register_blueprint(chat.bp)
    app.register_blueprint(auth_views.bp)

    return app
