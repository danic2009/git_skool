def cezar_shifr(mesege, shift):
    index_list = [(book_list[(book_list.index(sym) + shift) % 33]
                   if sym != ' ' else ' ') for sym in mesege]
    sym_list = ''
    for sym in index_list:
        sym_list += sym
    return sym_list


book_list = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

mesege = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
answer = cezar_shifr(mesege, shift)

print('Зашифрованное сообщение:', answer)

# зачтено
