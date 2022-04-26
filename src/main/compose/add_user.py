from typing import Dict
from src.presenters.controllers.user import AddUserController


class Validator:
    @staticmethod
    def validate(body: Dict = None) -> bool:
        return True


class AddUserUseCase:
    pass


def makeAddUserController():
    return AddUserController(AddUserUseCase(), Validator.validate)
