# Written by: Sepehr Bazyar
from cryptography.fernet import Fernet
from exceptions import KeyTypeError, WrongKeyError
from typing import Union


class Encrypt:
    def __new__(cls, key: Union[str, bytes]):
        if not isinstance(key, (str, bytes)):
            raise KeyTypeError(f"Can't Convert {type(key)} Object to Bytes.")
        try:
            Fernet(key if isinstance(key, bytes) else key.encode())
        except:
            raise WrongKeyError("Invalid Key.")
        else:
            return super().__new__(cls)

    def __init__(self, key: Union[str, bytes]) -> None:
        self.__key = key if isinstance(key, bytes) else key.encode()
        self.__frnt = Fernet(self.key)

    @property
    def key(self) -> bytes: return self.__key

    @key.setter
    def key(self, new_key: Union[str, bytes]) -> None:
        if not isinstance(new_key, (str, bytes)):
            raise KeyTypeError(
                f"Can't Convert {type(new_key)} Object to Bytes.")
        self.__key = new_key if isinstance(
            new_key, bytes) else new_key.encode()

    def __encrypt(self, text: str) -> bytes:
        return self.__frnt.encrypt(str(text).encode())

    def __call__(self, file_path: str) -> None:
        pass

    def __repr__(self) -> str:
        pass