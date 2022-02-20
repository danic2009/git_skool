import random

list_of_numbers = [random.randint(0, 2) for i in range(10)]
print(f'Кол-во чисел в списке: {len(list_of_numbers)}')
print(f'Список до сжатия: {list_of_numbers}')
list_clear = [i for i in list_of_numbers if i]
print(f'Список после сжатия: {list_clear}')

# зачтено
