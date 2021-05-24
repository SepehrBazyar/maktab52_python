# Written by: Sepehr Bazyar
from HW10_01_Validation import name_validation, email_validation, phone_validation
import json


class SignUp:
    USERS = []

    def __init__(self, name: str, phone: str, email: str) -> None:
        assert name_validation(name), "Just Char and Underline Between 5 & 14"
        assert phone_validation(phone), "Start with 09 or +989 and 9 Digits"
        assert email_validation(email), "Validate Sample: name@mail.com"
        self.name, self.phone, self.email = name, phone, email
        self.USERS.append(self)

    @classmethod
    def save(cls, path="users.json"):
        users_list = []
        for user in cls.USERS:
            users_list.append({
                "name": user.name,
                "phone": user.phone,
                "email": user.email
            })
        with open(path, 'w') as fl:
            json.dump(users_list, fl, indent=4)

    @classmethod
    def load(cls, path="users.json"):
        try:
            with open(path) as fl:
                users_list = json.load(fl)
            for user in users_list:
                SignUp(user["name"], user["phone"], user["email"])
        except:
            pass

    def __repr__(self) -> str:
        return f"""
<Name:  {self.name}>
<Phone: {self.phone}>
<Email: {self.email}>
"""
