# Written by: Sepehr Bazyar
from cryptography.fernet import Fernet
from .exceptions import KeyTypeError, WrongKeyError, FileNotFoundError
from typing import Union


class Decrypt:
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

    def __decrypt(self, secret: bytes) -> str:
        return self.__frnt.decrypt(secret).decode()

    def __call__(self, file_path: str) -> str:
        try:
            with open(file_path, 'rb') as fl:
                lines = fl.readlines()
        except:
            raise FileNotFoundError(f"No Such {file_path} File")
        else:
            decrypted = []
            for line in lines:
                decrypted.append(self.__decrypt(line.strip()))

            name = file_path.rsplit(
                '.', 1)[0] + "_decrypted." + file_path.rsplit('.', 1)[1]
            with open(name, 'w') as fl:
                print(*decrypted, sep='\n', file = fl)
            return name

    def __repr__(self) -> str:
        return f"<Decrypt Key: {self.__key.decode()}>"
