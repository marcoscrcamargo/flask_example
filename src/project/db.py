from flask_sqlalchemy import SQLAlchemy

db = None


def init_app(app):
    global db
    db = SQLAlchemy(app)

    return db

