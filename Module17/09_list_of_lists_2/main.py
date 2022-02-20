nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

l = [elem for elems in nice_list for elem in [item for items in elems for item in items]]
print(l)

# зачтено
