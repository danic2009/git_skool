text = input('Введите строку: ').split()
max_word = []
for i_text in range(len(text)):
    if len(text[i_text]) > len(max_word):
        max_word = text[i_text]
print('Самое длинное слово:', max_word)
print('Длина этого слова:', len(max_word))
