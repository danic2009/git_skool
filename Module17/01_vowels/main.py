simbol = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
symbol_text = [i for i in input('Введите фразу: ') if i in simbol]
print(f'Список гласных букв: {symbol_text}')
print(f'Длина списка: {len(symbol_text)}')

# зачтено
