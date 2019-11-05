from . import create_app
import logging

app = create_app()

# https://medium.com/@trstringer/logging-flask-and-gunicorn-the-manageable-way-2e6f0b8beb2f
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
