from typing import Callable
from src.presenters.helpers import HttpRequest

# addUserController.handle


def adpt(req: any, callback: Callable):
    body = req.get_json()
    requestData = HttpRequest({}, body, {})
    response = callback(requestData)
    return response
