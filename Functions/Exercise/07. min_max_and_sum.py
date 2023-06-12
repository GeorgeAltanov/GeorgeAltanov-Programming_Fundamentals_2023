
def max_min_sum_of_number(num):
    my_list = []

    for num in num:
        my_list.append(int(num))
    max_number = max(my_list)
    min_number = min(my_list)
    sum_number = sum(my_list)
    return max_number, min_number, sum_number

numbers = input().split()
max_num, min_num, sum_num = max_min_sum_of_number(numbers)
print(f"The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_num}")
