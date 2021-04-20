from enum import Enum


class ErrorCodes(str, Enum):
    already_exists = "already_exists"
    unexpected_error = "unexpected_error"
    successful = ""
