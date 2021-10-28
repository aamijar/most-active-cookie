"""
Module that represents the cookie dataclass
"""

LABEL_COOKIE = 'cookie'
LABEL_TIMESTAMP = 'timestamp'
LABEL_DATE = 'date'
LABEL_CODE = 'code'


class Cookie:

    def __init__(self, code, date):
        super().__init__()
        self.code = code
        self.date = date
    