def find_h(line):
    firs_h = symbol.index('h') + 1
    re = symbol[::-1]
    second_h = re.index('h') + 1
    rev = symbol[firs_h:-second_h]
    print(*rev[::-1])


symbol = [i for i in input('Введите строку: ')]
if 'h' in symbol and len(symbol) == 2:
    print('h')
elif 'h' in symbol:
    find_h(symbol)
else:
    print('h не обнаружен в строке')

# зачтено
