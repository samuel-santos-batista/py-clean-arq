from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class IController(ABC):
    @abstractmethod
    def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        raise Exception("Method not implemented")
