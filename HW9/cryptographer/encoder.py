# Written by: Sepehr Bazyar
from cryptography.fernet import Fernet
from .exceptions import KeyTypeError, WrongKeyError, FileNotFoundError
from typing import Union
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)-10s - %(message)s')


class Encrypt:
    def __new__(cls, key: Union[str, bytes]):
        if not isinstance(key, (str, bytes)):
            logging.error("Invalid Type for Key Encrypted.")
            raise KeyTypeError(f"Can't Convert {type(key)} Object to Bytes.")
        try:
            Fernet(key if isinstance(key, bytes) else key.encode())
        except:
            logging.error("Invalid Key for Encrypted.")
            raise WrongKeyError("Invalid Key.")
        else:
            logging.info("Validated Key Ready for Encrypt.")
            return super().__new__(cls)

    def __init__(self, key: Union[str, bytes]) -> None:
        self.__key = key if isinstance(key, bytes) else key.encode()
        self.__frnt = Fernet(self.__key)
        logging.debug("Create an Object for Encrypt with Key.")

    @property
    def key(self) -> bytes: return self.__key

    @key.setter
    def key(self, new_key: Union[str, bytes]) -> None:
        if not isinstance(new_key, (str, bytes)):
            logging.error("Invalid Type for Key Encrypted.")
            raise KeyTypeError(
                f"Can't Convert {type(new_key)} Object to Bytes.")
        self.__key = new_key if isinstance(
            new_key, bytes) else new_key.encode()
        self.__frnt = Fernet(self.__key)
        logging.info("Change Key Successfully.")

    def _encrypt(self, text: str) -> bytes:
        logging.debug("Try for Encrypted Text...")
        return self.__frnt.encrypt(text.encode())

    def __call__(self, file_path: str) -> str:
        try:
            with open(file_path) as fl:
                lines = fl.readlines()
            logging.debug("Read Text File Successfully.")
        except:
            logging.error("Not Found File in Directory.")
            raise FileNotFoundError(f"No Such {file_path} File")
        else:
            encrypted = []
            for line in lines:
                encrypted.append(self._encrypt(line.strip()))
            logging.debug("Encrypted All Lines of File.")

            name = file_path.rsplit(
                '.', 1)[0] + "_encrypted." + file_path.rsplit('.', 1)[1]
            with open(name, 'wb') as fl:
                for item in encrypted:
                    fl.write(item + b'\n')
            logging.warning(f"Write Encrypted Text in {name} File.")
            return name

    def __repr__(self) -> str:
        return f"<Encrypt Key: {self.__key.decode()}>"
