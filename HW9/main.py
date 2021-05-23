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
    parser.add_argument('-l', '--login', metavar="{SIGN_IN, SIGN_UP}", action='store',
                        choices=["sign_in", "sign_up"], required=True, help="Account Login Type")

    subprasers = parser.add_subparsers(
        dest='command', help="Cryptography Program Type")

    encr = subprasers.add_parser('encrypt', help="Encrypted File or Message")
    encr.add_argument('-m', '--message', action='store_true',
                      dest='file', help="Get Text Message in Console")
    encr.add_argument('-p', '--path', metavar="PATH", action='store',
                      type=str, help="Text File Address Location")

    decr = subprasers.add_parser('decrypt', help="Decrypted File or Message")
    decr.add_argument('-m', '--message', action='store_true',
                      dest='file', help="Get Secret Message in Console")
    decr.add_argument('-p', '--path', metavar="PATH", action='store',
                      type=str, help="Binary File Address Location")

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
        if args.command == "encrypt":
            enc = encoder.Encrypt(key)
            if not args.file:
                enc(args.path)
            else:
                lines, counter = [], 1
                while True:
                    try:
                        lines.append(input(f"#{counter} ") + '\n')
                        counter += 1
                    except KeyboardInterrupt:
                        break
                name = lines[0][: 31][: -1].replace(" ", "_")
                with open(f"{name}.txt", 'w') as fl:
                    fl.writelines(lines)
                enc(f"{name}.txt")
                remove(f"{name}.txt")

        elif args.command == "decrypt":
            dec = decoder.Decrypt(key)
            if not args.file:
                dec(args.path)
            else:
                lines, counter = [], 1
                while True:
                    try:
                        lines.append(input(f"#{counter} ").encode() + b'\n')
                        counter += 1
                    except KeyboardInterrupt:
                        break
                name = lines[0][: 31][: -1].replace(" ", "_").decode()
                with open(f"{name}.txt", 'wb') as fl:
                    fl.writelines(lines)
                dec(f"{name}.txt")
                remove(f"{name}.txt")

        else:
            raise exceptions.InvalidInputError("Just Encrypt or Decrypt.")
