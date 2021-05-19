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
        pass
