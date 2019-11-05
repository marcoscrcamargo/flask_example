from flask_migrate import Migrate


def init_app(app):
    app.migrade = Migrate(app, app.db)
