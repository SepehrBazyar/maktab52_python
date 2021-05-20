# Written by: Sepehr Bazyar
from cryptographer import generator, encoder, decoder, exceptions
from typing import Callable
import argparse, os


class SecretOpen:
    def __init__(self, file_path: str, key: bytes) -> None:
        self.file_path, self._key = file_path, key
        self.__enc, self.__dec = encoder.Encrypt(key), decoder.Decrypt(key)

    def __enter__(self):
        self._path = self.__dec(self.file_path)
        self._file = open(self._path, 'ab')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self._file.close()
            self._name = self.__enc(self._path)
            with open(self._name, 'rb') as copy:
                with open(self.file_path, 'wb') as secret:
                    secret.writelines(copy.readlines())
            os.remove(self._path); os.remove(self._name)
        return True


def encrypt(key: bytes):
    def wrapper(function: Callable):
        def inner(*args, **kwargs):
            result = function(*args, **kwargs)
            answer = encoder.Encrypt(key)._encrypt(result)
            return answer
        return inner
    return wrapper


if __name__ == '__main__':
    name = input("Username: ")
    try:
        user = generator.KeyGenerator(name)
    except:
        key = generator.KeyGenerator._keys[name.encode().hex()]
    else:
        key = user.key
    finally:
        code = input("""
1. Encrypt
2. Decrypt

>>> """)
        if code == '1':
            enc = encoder.Encrypt(key)
            enc(input("File Address: "))
        else:
            dec = decoder.Decrypt(key)
            dec(input("File Address: "))
