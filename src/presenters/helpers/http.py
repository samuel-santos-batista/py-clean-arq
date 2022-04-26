from typing import Dict


class HttpRequest:
    def __init__(self, header: Dict = None, body: Dict = None, params: Dict = None) -> None:
        self.header = header
        self.body = body
        self.params = params


class HttpResponse:
    def __init__(self, status_code: int, body: Dict = None) -> None:
        self.status_code = status_code
        self.body = body
