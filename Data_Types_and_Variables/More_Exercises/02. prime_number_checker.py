# Write a program to check if a number is prime.
# A prime number is a natural number greater than 1, not a product of two smaller natural numbers.
# For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
# The input comes as an integer number.
# The output should be True if the number is prime and False otherwise.
#
# Input1: 7
# Output1: True
# Input2: 8
# Output2: False
# Input3: 81
# Output3: False


number = int(input())

flag = False

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            flag = True
            break

if flag or number == 1:
    print("False")

else:
    print("True")
