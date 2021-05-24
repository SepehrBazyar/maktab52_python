# Written by: Sepehr Bazyar
import re as regex


def name_validation(name: str) -> bool:
    "Lenght of Username Between 5 to 14 and Only has Char and Underline."
    # ^ for check in start of string and $ for end of string
    pattern = "^[A-Za-z\_]{5,14}$"
    return bool(regex.search(pattern, name))


def email_validation(email: str) -> bool:
    "name@mail.com is a Validate Email because has a Username and a Domain Name."
    # split by group items and domain name musn't end with dot char
    pattern = r"^([\w\.\_\-]+)[@]([\w\.\_\-]*\w)[.]([A-Za-z]{2,3})$"
    return bool(regex.search(pattern, email))


def phone_validation(phone: str) -> bool:
    "Phone Number Must be Start with 09 or +989 and Lenght's is 11 or 13."
    # after pre number each group 1 must be have 9 digits
    pattern = r"^(09|\+989)(\d{9})$"
    return bool(regex.search(pattern, phone))
