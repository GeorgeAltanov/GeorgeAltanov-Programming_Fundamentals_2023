def calculate_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number

first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_factorial(first_number)
second_number_factorial = calculate_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")




# def division(some_number_1, some_number_2):
#     factorial_1 = 1
#     factorial_2 = 1
#     for num in range(1, number_1 + 1):
#         factorial_1 *= num
#     for num in range(1, number_2 + 1):
#         factorial_2 *= num
#     result = factorial_1 / factorial_2
#     return f"{result:.2f}"
#
#
# number_1 = int(input())
# number_2 = int(input())
#
# print(division(number_1, number_2))
