from flask import Flask, render_template
from .extensions import db, login_manager
from .routes import register_app
from .models import Admin
from decouple import config


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = config('SECRET_KEY')

    DB_USER = config('DB_USER')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_NAME = config('DB_NAME')
    DB_HOST = config('DB_HOST', default='localhost')
    DB_PORT = config('DB_PORT', default=5432)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     

    db.init_app(app)

    register_app(app)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))


    return app