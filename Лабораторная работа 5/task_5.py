import random
from random import sample

chars = '3456erdtfcvgi874rtfguERDFCYUuhbIUH341230DFYVYGVUHBfgqazxrfvFVUIOKUNBFG7890'

def get_random_password() -> str:
    length = 8
    password = "".join(random.sample(chars, length))
    return password

print(get_random_password())
