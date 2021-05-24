# Written by: Sepehr Bazyar
from HW10_01_Validation import name_validation, email_validation, phone_validation
import json


class SignUp:
    USERS = []  # class attribute for save all instance of SignUp

    def __init__(self, name: str, phone: str, email: str) -> None:
        assert name_validation(name), "Just Char and Underline Between 5 & 14"
        assert phone_validation(phone), "Start with 09 or +989 and 9 Digits"
        assert email_validation(email), "Validate Sample: name@mail.com"
        self.name, self.phone, self.email = name, phone, email
        self.USERS.append(self)  # appending object created to class list

    @classmethod
    def save(cls, path="users.json"):
        users_list = []  # creat list of user attr for dumping to json file
        for user in cls.USERS:
            users_list.append({
                "name": user.name,
                "phone": user.phone,
                "email": user.email
            })
        with open(path, 'w') as fl:
            json.dump(users_list, fl, indent=4)  # indent for better showing

    @classmethod
    def load(cls, path="users.json"):
        try:
            with open(path) as fl:
                users_list = json.load(fl)  # get list contains user and attrs
            for user in users_list:
                SignUp(user["name"], user["phone"], user["email"])  # creating
        except:  # if file not found and for first time run program
            pass

    def __repr__(self) -> str:
        return f"""
<Name:  {self.name}>
<Phone: {self.phone}>
<Email: {self.email}>
"""
