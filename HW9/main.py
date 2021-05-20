# Written by: Sepehr Bazyar
from cryptographer import generator, encoder, decoder, exceptions
from typing import Callable
from os import remove
import argparse


class SecretOpen:
    def __init__(self, file_path: str, key: bytes) -> None:
        self.file_path = file_path
        self.__enc, self.__dec = encoder.Encrypt(key), decoder.Decrypt(key)

    def __enter__(self):
        self._decoding = self.__dec(self.file_path)
        self._file = open(self._decoding, 'a')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self._file.close()
            self._encoding = self.__enc(self._decoding)
            with open(self._encoding, 'rb') as copy:
                with open(self.file_path, 'wb') as secret:
                    secret.writelines(copy.readlines())
            remove(self._decoding)
            remove(self._encoding)
        return True


def encrypt(key: bytes):
    def wrapper(function: Callable):
        def inner(*args, **kwargs):
            result = function(*args, **kwargs)
            answer = encoder.Encrypt(key)._encrypt(result)
            return answer
        return inner
    return wrapper


@encrypt(key)
def say_hello(name: str) -> str:
    return f"Hello {name}"


if __name__ == '__main__':
    name = input("Username: ")
    try:
        user = generator.KeyGenerator(name)
    except:
        key = generator.KeyGenerator._keys[name.encode().hex()]
    else:
        key = user.key
    finally:
        print('\n', say_hello(name).decode())
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
