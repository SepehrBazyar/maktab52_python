# Written by: Sepehr Bazyar
from cryptography.fernet import Fernet
import pickle, logging


class KeyGenerator:
    __keys = {}

    def __init__(self, username: str) -> None:
        self.username = username
        self.__ID = self.username.encode().hex()
        self.__key = Fernet.generate_key()
        self.__class__.__keys[self.__ID] = self.__key

    @property
    def key(self) -> bytes: return self.__key

    @classmethod
    def save_file(cls, path_file: str = ".\\encrypts.key") -> None:
        with open(path_file, 'wb') as fl:
            pickle.dump(cls.__keys, fl)

    def __repr__(self) -> str:
        return f"<{self.username}: {self.__key.decode()}>"
