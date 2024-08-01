import http

from flask import Blueprint, request

from src.controllers.user_controller import UserController
from src.db import session_scope

user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.route("", methods=["GET"])
def get_users():
    with session_scope() as session:
        user_controller = UserController(session)
        users = user_controller.get_users()

        return {"data": users}, http.HTTPStatus.OK
