from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api

# Объявляем базу данных
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Инициализируем базу в приложении:
    db.init_app(app)
    with app.app_context():

        api = Api(app)
        app.config["api"] = api

        from application import routes

        return app