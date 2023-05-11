from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "Corona.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcde'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .add_employee import add_employee
    from .show_employee import show_employee

    app.register_blueprint(add_employee, url_prefix='/')
    app.register_blueprint(show_employee, url_prefix='/')

    from .models import Employee, Vaccine, Covid_cases

    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
