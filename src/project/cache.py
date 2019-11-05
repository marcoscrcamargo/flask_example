from flask_caching import Cache

cache = None


def init_app(app):
    global cache
    cache = Cache(app)
    return cache
