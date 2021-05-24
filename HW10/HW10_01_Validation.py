# Written by: Sepehr Bazyar
import re as regex


def name_validation(name: str) -> bool:
    "Lenght of Username Between 5 to 14 and Only has Char and Underline."
    pattern = "^[A-Za-z\_]{5,14}$" # ^ for check in start string and $ for end of string
    return bool(regex.search(pattern, name))


def email_validation(email: str) -> bool:
    pass


def phone_validation(phone: str) -> bool:
    pass
