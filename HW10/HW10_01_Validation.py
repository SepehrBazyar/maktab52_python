# Written by: Sepehr Bazyar
import re as regex


def name_validation(name: str) -> bool:
    "Lenght of Username Between 5 to 14 and Only has Char and Underline."
    pattern = "^[A-Za-z\_]{5,14}$" # ^ for check in start string and $ for end of string
    return bool(regex.search(pattern, name))


def email_validation(email: str) -> bool:
    "name@mail.com is a Validate Email because has a Username and a Domin Name."
    pattern = r"^([\w\.\_\-]+)[@]([\w\.\_\-]*\w)[.]([A-Za-z]{2,3})$" # split by group items
    return bool(regex.search(pattern, email))


def phone_validation(phone: str) -> bool:
    pass
