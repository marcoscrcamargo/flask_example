from flask_restplus import Namespace, Resource, fields, reqparse
from project.cache import cache
from project.db import db
from project.blueprint.users.models import User

ns = Namespace("users", description="Manage users")

user_model = ns.model(
    "User", {"username": fields.String, "id": fields.Integer, "is_admin": fields.Boolean}
)


get_parse = reqparse.RequestParser()
get_parse.add_argument(
    "is_admin", required=False, help="Filter users by admin type", type=bool, dest="is_admin"
)


@ns.route("/")
class Get(Resource):
    @cache.cached(timeout=10, query_string=True)
    @ns.expect(get_parse)
    @ns.marshal_with(user_model)
    def get(self):
        args = get_parse.parse_args()
        query = db.session.query(User)

        if args.is_admin:
            query = query.filter(User.is_admin == args.is_admin)

        return query.all()

    def post(self):
        user = User(**ns.payload)
        db.session.add(user)
        db.session.commit()

        return {"message": "sucess"}, 200


@ns.route("/<string:id>")
class GetById(Resource):
    @cache.cached(timeout=10)
    @ns.marshal_with(user_model)
    def get(self, id):
        query = db.session.query(User).filter(User.id == id)

        return query.first()

    def post(self, id):
        user = db.session.query(User).filter(User.id == id).first()
        user.update(**ns.payload)
        db.session.merge(user)
        db.session.commit()

        return {"message": "sucess"}, 200

    def delete(self, id):
        query = db.session.query(User)
        query = query.filter(User.id == id)
        query.delete()
        db.session.commit()

        return {"message": "sucess"}, 200

