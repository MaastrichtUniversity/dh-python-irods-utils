"""This module contains a custom exception class"""


class ValidationError(Exception):
    """Exception raised for errors during validation

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "ValidationError, {}".format(self.message)
