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
