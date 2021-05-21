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
    parser.add_argument('-l', '--login', metavar="{SIGN_IN, SIGN_UP}", action='store', choices=[
                        "sign_in", "sign_up"], required=True, help="Account Login Type")

    # subprasers = parser.add_subparsers(dest='command')
    # blame = subprasers.add_parser('blame', help='blame people')
    # blame.add_argument(
    #     '--dry-run',
    #     help='do not blame, just pretend',
    #     action='store_true'
    # )
    # blame.add_argument('name', nargs='+', help='name(s) to blame')
    # praise = subprasers.add_parser('praise', help='praise someone')
    # praise.add_argument('name', help='name of person to praise')
    # praise.add_argument(
    #     'reason',
    #     help='what to praise for (optional)',
    #     default="no reason",
    #     nargs='?'
    # )

    args = parser.parse_args()

    user_pass = {}
    try:
        with open(".\\cryptographer\\users.pass", 'rb') as fl:
            user_pass.update(pickle.load(fl))
    except:
        pass

    username = input("Username: ")
    password = sha256(getpass("Password: ").encode()).hexdigest()
    if args.login == "sign_up":
        re_password = sha256(getpass("Repeat Password: ").encode()).hexdigest()
        if re_password != password:
            raise exceptions.PasswordMatchingError("Password Not Match.")
        if username not in user_pass:
            user_pass[username] = password
            with open(".\\cryptographer\\users.pass", 'wb') as fl:
                pickle.dump(user_pass, fl)
        else:
            raise exceptions.DuplicateUserError("User Name is Already in Use.")
    else:
        if username in user_pass:
            if user_pass[username] != password:
                raise exceptions.WrongPasswordError("Wrong Password.")
        else:
            raise exceptions.UserNotFoundError("Wrong User Name.")

    try:
        user = generator.KeyGenerator(username)
    except:
        key = generator.KeyGenerator._keys[username.encode().hex()]
    else:
        key = user.key
    finally:
        @encrypt(key)
        def say_hello(name: str) -> str:
            return f"Hello {name}!"

        print('\n', say_hello(username).decode())
