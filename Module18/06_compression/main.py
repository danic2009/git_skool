line = input('Введите строку: ')
count = 0
new_line = ''
for i in range(len(line)):
    count += 1
    if i == len(line) - 1:
        new_line = new_line + line[i] + str(count)
        break
    if line[i] != line[i+1]:
        new_line = new_line + line[i] + str(count)
        count = 0
print(f'Закодированная строка: {new_line}')
