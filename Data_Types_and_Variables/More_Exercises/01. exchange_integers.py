# Read two integer numbers and, after that, exchange their values. Print the variable values before and after the exchange
#
# Input1:
# 5
# 10
#
# Output1:
# Before:
# a = 5
# b = 10
# After:
# a = 10
# b = 5
#
# Input2:
# 10
# 20
#
# Output2:
# Before:
# a = 10
# b = 20
# After:
# a = 20
# b = 10



first_number = int(input())
second_number = int(input())

third_number = second_number
fourth_number = first_number

print(f"Before:\n"
      f"a = {fourth_number}\n"
      f"b = {second_number}\nAfter:\n"
      f"a = {third_number}\n"
      f"b = {first_number}")
