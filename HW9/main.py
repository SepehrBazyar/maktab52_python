# Written by: Sepehr Bazyar
from cryptographer import generator, encoder, decoder, exceptions
from typing import Callable
import argparse

def encrypt(key: bytes):
    def wrapper(functions: Callable):
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
