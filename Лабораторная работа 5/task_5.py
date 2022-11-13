import random
from random import sample

chars = '3456erdtfcvgi874rtfguERDFCYUuhbIUH341230DFYVYGVUHBfgqazxrfvFVUIOKUNBFG7890'

def get_random_password() -> str:

    password = "".join(random.sample(chars, 8))
    return password

print(get_random_password())
