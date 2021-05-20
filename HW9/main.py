# Written by: Sepehr Bazyar
from cryptographer import generator, encoder, decoder, exceptions

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
