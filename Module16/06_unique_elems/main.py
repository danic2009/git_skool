firs_list = []
second_list = []

for i in range(3):
    x = int(input(f'Введите {i + 1} число для первого списка: '))
    firs_list.append(x)

for i in range(7):
    x = int(input(f'Введите {i + 1} число для первого списка: '))
    second_list.append(x)

print(f'Первый список: {firs_list}')
print(f'Второй список: {second_list}')

firs_list.extend(second_list)
for j in firs_list:
    count = firs_list.count(j)
    while firs_list.count(j) != 1:
        firs_list.remove(j)
print(f'\nНовый первый список с уникальными элементами: {firs_list}')

# зачтено
