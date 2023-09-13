# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().
# The output should be as follows:
# • On the first line: "The minimum number is {minimum number}"
# • On the second line: "The maximum number is {maximum number}"
# • On the third line: "The sum number is: {sum of all numbers}"
#
# Input1: 2 4 6
# Output1:
# The minimum number is 2
# The maximum number is 6
# The sum number is: 12
#
# Input2: 12 52 11 53 2 8 45
# Output2:
# The minimum number is 2
# The maximum number is 53
# The sum number is: 183


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
