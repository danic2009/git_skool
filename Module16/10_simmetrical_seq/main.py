def is_palindrome(num_list):
    revers_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        revers_list.append(num_list[i_num])
    if num_list == revers_list:
        return True
    else:
        return False


sum_nam = int(input('Кол-во чисел: '))
nums = []
nuw_nums = []
answer = []

for _ in range(sum_nam):
    n = int(input('Число: '))
    nums.append(n)

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        nuw_nums.append(nums[j_elem])
    if is_palindrome(nuw_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    nuw_nums = []

print(f'Последовательность: {nums}')
print(f'Нужно приписать чисел: {len(answer)}')
print(f'Сами числа: {answer}')

# зачтено
