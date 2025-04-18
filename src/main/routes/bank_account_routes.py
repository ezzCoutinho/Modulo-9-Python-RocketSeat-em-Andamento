from flask import Blueprint, jsonify, request

from src.composer.balance_editor_composer import balance_editor_composer
from src.composer.login_creator_composer import login_creator_composer
from src.composer.user_register_composer import user_register_composer
from src.main.middlewares.auth_jwt import auth_jwt_verify
from src.views.http_types.http_request import HttpRequest
from src.errors.error_controller import handle_errors

bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json or {})
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        response = handle_errors(error)
        return jsonify(response["body"]), response["status_code"]


@bank_routes_bp.route("/bank/login", methods=["POST"])
def login():
    try:
        http_request = HttpRequest(body=request.json or {})
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        response = handle_errors(error)
        return jsonify(response["body"]), response["status_code"]


@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"])
def balance_editor(user_id: str):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json or {},
            params={"user_id": user_id},
            token_info=token_information,
            headers=request.headers,
        )
        http_response = balance_editor_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        response = handle_errors(error)
        return jsonify(response["body"]), response["status_code"]
