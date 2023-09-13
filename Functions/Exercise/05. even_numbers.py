# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().
#
# Input1: 1 2 3 4
# Output1: [2, 4]
#
# Input2: 1 2 3 -1 -2 -3
# Output2: [2, -2]


def even_numbers(num):
    result = []

    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            num = str(num)
            result.append(num)
    l = list(map(int, result))
    return l

numbers = input().split()

print(even_numbers(numbers))


# def is_even(number):
#     if number % 2 == 0:
#         return number
#
# numbers_as_string = input().split()
# numbers_as_digits = []
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))
# #numbers_as_digits = [int(number) for number in numbers-as_string]
# result = list(filter(is_even, numbers_as_digits))
# print(result)
