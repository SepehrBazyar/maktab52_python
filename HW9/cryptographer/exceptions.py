# Written by: Sepehr Bazyar
class WrongKeyError(Exception):
    "Error When Base of Encrypt or Decrypt on a Worng Key."


class KeyNotFoundError(Exception):
    "Error When Not Found Key of User in the File."


class KeyTypeError(Exception):
    "Error When Get Invalid Key Because Type Not Bytes or Str."


class FileNotFoundError(FileNotFoundError):
    "Built-in Error in Exception Module at Not Found File."


class DuplicateUserError(Exception):
    "Error When Create New User with Usage Username."
