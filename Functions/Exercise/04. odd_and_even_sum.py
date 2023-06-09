
def even_sum(num):
    result = 0
    for num in number:
        num = int(num)
        if num % 2 == 0:
            result += num
    return result


def odd_sum(num):
    result = 0
    for num in number:
        num = int(num)
        if num % 2 != 0:
            result += num
    return result


number = input()
print(f"Odd sum = {odd_sum(number)}, Even sum = {even_sum(number)}")


# def odd_even_numbers(some_number):
#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0
#     for digit in some_number:
#         if int(digit) % 2 == 0:
#             sum_of_even_digits += int(digit)
#         else:
#             sum_of_odd_digits += int(digit)
#     return sum_of_odd_digits, sum_of_even_digits
#
#
# number = input()
# odd_digits, even_digits = odd_even_numbers(number)
# print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")