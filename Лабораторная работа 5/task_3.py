from random import randint
from time import time

def get_unique_list_numbers(start=-10,stop=10,size=15):
    list_=[]
    if stop - start >= size:
        while len(list_) < size:
            x = randint(start,stop)
            if x not in list_:
                list_.append(x)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
