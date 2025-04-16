from flask import Blueprint, jsonify, request

from src.composer.balance_editor_composer import balance_editor_composer
from src.composer.login_creator_composer import login_creator_composer
from src.composer.user_register_composer import user_register_composer
from src.views.http_types.http_request import HttpRequest

bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    http_request = HttpRequest(body=request.json or {})
    http_response = user_register_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route("/bank/login", methods=["POST"])
def login():
    http_request = HttpRequest(body=request.json or {})
    http_response = login_creator_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"])
def balance_editor(user_id: str):
    http_request = HttpRequest(body=request.json or {}, params={"user_id": user_id})
    http_response = balance_editor_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code
