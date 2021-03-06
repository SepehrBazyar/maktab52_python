# Written by: Sepehr Bazyar
class WrongKeyError(Exception):
    "Error When Base of Encrypt or Decrypt on a Worng Key."


class KeyNotFoundError(Exception):
    "Error When Not Found Key of User in the File."


class KeyTypeError(Exception):
    "Error When Get Invalid Key Because Type Not Bytes or Str."


class FileNotFoundError(Exception):
    "Built-in Error in Exception Module at Not Found File."


class DuplicateUserError(Exception):
    "Error When Create New User with Usage Username."


class WrongPasswordError(Exception):
    "Error When Enter Wrong Password for Login."


class PasswordMatchingError(Exception):
    "Error When Not Match Pass and Repeated Pass in Sign Up."


class UserNotFoundError(Exception):
    "Error When Sign in User with Wrong User Name."


class InvalidInputError(Exception):
    "Error When Get Invalid Input in Each Other."
