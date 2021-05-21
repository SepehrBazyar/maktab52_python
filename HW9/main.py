# Written by: Sepehr Bazyar
from cryptographer import generator, encoder, decoder, exceptions
from typing import Callable
from os import remove
from hashlib import sha256
from getpass import getpass
import argparse
import pickle


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="<Encrypt & Decrypt Message>")
    parser.add_argument('-l', '--login', metavar="ACCOUNT", action='store',
                        choices=["sign in", "sign up"], required=True, help="Login Type")
    args = parser.parse_args()

    user_pass = {}
    try:
        with open(".\\cryptographer\\users.pass", 'rb') as fl:
            user_pass.update(pickle.load(fl))
    except: pass

    username = input("Username: ")
    password = sha256(getpass("Password: ").encode()).hexdigest()
    if args.username == "sign up":
        re_password = sha256(getpass("Repeat Password: ").encode()).hexdigest()
        if re_password != password:
            raise exceptions.PasswordMatchingError("Password Not Match.")
        user_pass[username] = password
        with open(".\\cryptographer\\users.pass", 'wb') as fl:
            pickle.dump(user_pass, fl)
    else:
        if user_pass[username] != password:
            raise exceptions.WrongPasswordError("Wrong Password.")

    try:
        user = generator.KeyGenerator(args.username)
    except:
        key = generator.KeyGenerator._keys[args.username.encode().hex()]
    else:
        key = user.key
    finally:
        @encrypt(key)
        def say_hello(name: str) -> str:
            return f"Hello {name}!"

        print('\n', say_hello(args.username).decode())
