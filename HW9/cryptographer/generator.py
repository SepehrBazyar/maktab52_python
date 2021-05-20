# Written by: Sepehr Bazyar
from cryptography.fernet import Fernet
from .exceptions import DuplicateUserError
import pickle
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)-10s - %(message)s')


class KeyGenerator:
    _keys = {}

    def __new__(cls, username: str):
        try:
            with open(".\\cryptographer\\encrypts.key", 'rb') as fl:
                cls._keys.update(pickle.load(fl))
                logging.debug("Read Key of Users by the File.")
        except:
            pass

        if username.encode().hex() not in cls._keys:
            logging.info("Create User Successfully.")
            return super().__new__(cls)
        else:
            logging.error('Error at Create Duplicate User.')
            raise DuplicateUserError(
                f"The {username} Name has Already Existed.")

    def __init__(self, username: str) -> None:
        self.__username = username
        self.__ID = username.encode().hex()
        self.__key = Fernet.generate_key()
        logging.debug("Generate an ID's and a Key's for User.")
        self.__class__._keys[self.__ID] = self.__key
        self.__save_file()

    @property
    def username(self) -> str: return self.__username

    @username.setter
    def username(self, new_username: str) -> None:
        new_ID = new_username.encode().hex()
        if new_ID in self.__class__._keys:
            logging.error('Error at Change Name Duplicate User.')
            raise DuplicateUserError(
                f"The {new_username} Name Already Existed.")
        self.__class__._keys[new_ID] = self.__class__._keys.pop(self.__ID)
        self.__username, self.__ID = new_username, new_ID
        logging.debug("Changed the ID's and a Key's for User.")
        self.__save_file()

    @property
    def key(self) -> bytes: return self.__key

    @classmethod
    def __save_file(cls) -> None:
        with open(".\\cryptographer\\encrypts.key", 'wb') as fl:
            pickle.dump(cls._keys, fl)
        logging.info("Save User Information into the File.")

    def __del__(self):
        self.__class__._keys.pop(self.__ID)
        self.__save_file()
        logging.warning("Deleted User and Key's from the File.")

    def __repr__(self) -> str:
        return f"<{self.__username}: {self.__key.decode()}>"
