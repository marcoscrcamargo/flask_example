from flask import Flask
from flask_cors import CORS
import os
import sqlalchemy


class Config(object):
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "flask_example")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)

    SQLALCHEMY_DATABASE_URI = "postgresql://%s:%s@%s:%s/%s" % (
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DATABASE,
    )
    CACHE_TYPE = "redis"
    CACHE_REDIS_HOST = os.environ.get("REDISHOST", "localhost")
    CACHE_REDIS_PORT = int(os.environ.get("REDISPORT", 6379))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "pool_pre_ping": True,
        "pool_recycle": 2 * 60 * 60,
        "poolclass": sqlalchemy.pool.SingletonThreadPool,
    }


def create_app():
    from . import db, cache, migration, blueprint

    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    app.db = db.init_app(app)
    app.cache = cache.init_app(app)
    app.migration = migration.init_app(app)
    blueprint.init_app(app)

    return app

