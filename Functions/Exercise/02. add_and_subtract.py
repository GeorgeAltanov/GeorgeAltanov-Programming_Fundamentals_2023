# You will receive three integer numbers.
# Write functions named:
# • sum_numbers() that returns the sum of the first two integers
# • subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.
#
# Input1:
# 23
# 6
# 10
#
# Output1: 19
#
# Input2:
# 1
# 17
# 30
#
# Output2: -12
#
# Input3:
# 42
# 58
# 100
#
# Output3: 0



def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(sum_numbers, num_3):
    return sum_numbers - num_3


def add_and_subtract(num_1, num_2, num_3):
    sum_of_first_and_second_numbers = sum_numbers(num_1, num_2)
    result = subtract(sum_of_first_and_second_numbers, num_3)
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))
