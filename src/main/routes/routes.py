from flask import jsonify, request, Blueprint
from src.main.compose import makeAddUserController
from src.main.adpters import adpt

router_bp = Blueprint('any', __name__)


@router_bp.route('/user', methods=["POST"])
def hello_user():
    data = adpt(request, makeAddUserController().handle)
    if(isinstance(data, dict)):
        print("Acertou mireravi!!")
    return jsonify(data.body), data.status_code
