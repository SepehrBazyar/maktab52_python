# Written by: Sepehr Bazyar
from HW10_01_Validation import name_validation, email_validation, phone_validation
import json


class SignUp:
    def __init__(self, name: str, phone: str, email: str) -> None:
        assert name_validation(name), "Just Char and Underline Between 5 & 14"
        assert phone_validation(phone), "Start with 09 or +989 and 9 Digits"
        assert email_validation(email), "Validate Sample: name@mail.com"
        self.name, self.phone, self.email = name, phone, email

    