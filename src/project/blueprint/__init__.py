from flask import Blueprint, Flask, url_for
from flask_restplus import Api, apidoc
from flask_restplus import Namespace, Resource, reqparse


class Custom_API(Api):
    @property
    def specs_url(self):
        """
        The Swagger specifications absolute url (ie. `swagger.json`)

        :rtype: str
        """
        return url_for(self.endpoint("specs"), _external=False)

    def _register_apidoc(self, app: Flask) -> None:
        conf = app.extensions.setdefault("restplus", {})
        custom_apidoc = apidoc.Apidoc(
            "restplus_doc",
            "flask_restplus.apidoc",
            template_folder="templates",
            static_folder="static",
            static_url_path="/api/v1",
        )

        @custom_apidoc.add_app_template_global
        def swagger_static(filename: str) -> str:
            return url_for("restplus_doc.static", filename=filename)

        if not conf.get("apidoc_registered", False):
            app.register_blueprint(custom_apidoc)
        conf["apidoc_registered"] = True


def init_app(app):
    from . import users

    blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

    api = Custom_API(
        blueprint,
        title="Example API endpoint",
        version="1.0",
        descript="An example of API build in Pyhton using flask_restfull framework",
        doc="/docs/",
    )

    app.register_blueprint(blueprint, url_prefix="/api/v1")

    # Bring in the rest of our API code here

    from .users.routes import ns as ns_users

    api.add_namespace(ns_users)

    users.init_app(app)
