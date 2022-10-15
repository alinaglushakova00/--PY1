list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
#индекс максимального элемента
MAXIMUM_INDEX=list_numbers[0] #пусть первый элемент будет самым высоким
for current_index in list_numbers: #перебираем каждый элемент
     if current_index > MAXIMUM_INDEX: #если текущий элемент больше того,который встречали ранее
         MAXIMUM_INDEX = current_index #то перезаписываем максимальный

# TODO Оформить решение
MAXIMUM_INDEX = list_numbers.index(max(list_numbers))
list_numbers[-1],list_numbers[MAXIMUM_INDEX] = list_numbers[MAXIMUM_INDEX],list_numbers[-1]

print(list_numbers)
