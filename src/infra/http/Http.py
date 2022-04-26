from abc import ABC, abstractmethod


class Http(ABC):
    @abstractmethod
    def route(self, method: str, url: str, callback: any) -> None:
        raise Exception("Method not found")

    @abstractmethod
    def listen(self, port: int) -> None:
        pass
