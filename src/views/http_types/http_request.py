from typing import Dict


class HttpRequest:
    def __init__(
        self,
        body: Dict = None,
        headers: Dict = None,
        param: Dict = None,
        token_info: Dict = None,
    ) -> None:
        self.body = body
        self.headers = headers
        self.param = param
        self.token_info = token_info
