def check(first, second):
    step = 1
    test = False
    while step <= len(second):
        n = first[-step:] + first[:-step]
        if n == second:
            test = True
        step += 1
    return test
first = 'abcd'
second = 'cdba'
if check(first, second):
    print('Первая строка получается из второй со сдвигом', first.index(second[0]))
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')