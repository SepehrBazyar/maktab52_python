# Written by: Sepehr Bazyar
from cryptography.fernet import Fernet
from exceptions import DuplicateUserError
import pickle


class KeyGenerator:
    __keys = {}

    def __new__(cls, username: str):
        try:
            with open(".\\encrypts.key", 'rb') as fl:
                cls.__keys.update(pickle.load(fl))
        except:
            pass

        if username.encode().hex() not in cls.__keys:
            return super().__new__(cls)
        else:
            raise DuplicateUserError(f"The {username} Name has Already Existed.")

    def __init__(self, username: str) -> None:
        self.__username = username
        self.__ID = username.encode().hex()
        self.__key = Fernet.generate_key()
        self.__class__.__keys[self.__ID] = self.__key
        self.__save_file()

    @property
    def username(self) -> str: return self.__username

    @username.setter
    def username(self, new_username: str) -> None:
        new_ID = new_username.encode().hex()
        if new_ID in self.__class__.__keys:
            raise DuplicateUserError(
                f"The {new_username} Name Already Existed.")
        self.__class__.__keys[new_ID] = self.__class__.__keys.pop(self.__ID)
        self.__username, self.__ID = new_username, new_ID
        self.__save_file()

    @property
    def key(self) -> bytes: return self.__key

    @classmethod
    def __save_file(cls) -> None:
        with open(".\\encrypts.key", 'wb') as fl:
            pickle.dump(cls.__keys, fl)

    def __del__(self):
        self.__class__.__keys.pop(self.__ID)
        self.__save_file()

    def __repr__(self) -> str:
        return f"<{self.__username}: {self.__key.decode()}>"
