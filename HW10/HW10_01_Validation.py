# Written by: Sepehr Bazyar
import re as regex


def name_validation(name: str) -> bool:
    pattern = "^[A-Za-z\_]{5,14}$"
    return bool(regex.search(pattern, name))


def email_validation(email: str) -> bool:
    pass


def phone_validation(phone: str) -> bool:
    pass
