from operator import is_not
from pickle import NONE
from src.main.contracts import IController
from src.presenters.helpers import HttpResponse, HttpRequest
from typing import Type


class AddUserController(IController):
    def __init__(self, addUserUseCase, validator) -> None:
        self.addUserUseCase = addUserUseCase
        self.validator = validator

    def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        if httpRequest is None:
            return HttpResponse(status_code=400, body={})
        is_valid = self.validator(httpRequest.body)
        if is_valid:
            return HttpResponse(status_code=200, body={"msg": "VALAR DOHERIS"})
