# Written by: Sepehr Bazyar
from cryptography.fernet import Fernet
from exceptions import KeyTypeError
from typing import Union


class Encrypt:
    def __new__(cls, key: Union[str, bytes]):
        if not isinstance(key, (str, bytes)):
            raise KeyTypeError(f"Can't Convert {type(key)} Object to Bytes.")
        return super().__new__(cls)

    def __init__(self, key: Union[str, bytes]) -> None:
        self.key = key if isinstance(key, bytes) else key.encode()
        self.frnt = Fernet(self.key)

    def __encrypt(self, text: str) -> bytes:
        return self.frnt.encrypt(str(text).encode())

    def __call__(self, file_path: str) -> None:
        pass