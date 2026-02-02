class BizException(Exception):
    """业务异常"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class AuthException(Exception):
    """鉴权异常"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)