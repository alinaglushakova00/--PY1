from random import randint
from time import time

def get_unique_list_numbers():
    list_=[]
    while len(list_) < 15:
        x = randint(-10,10)
        if x not in list_:
            list_.append(x)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
