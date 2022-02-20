def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict



text = input('Введите текс: ').lower()
hist = histogram(text)
print(hist)
asdfadsfasdf