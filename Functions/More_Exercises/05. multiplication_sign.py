# You will receive three integer numbers.
# Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.
#
# Input1:
# 2
# 3
# -1
#
# Output1: negative
#
# Input2:
# 2
# 3
# 1
#
# Output2: positive



def multiplication(n_1, n_2, n_3):
    result = ""
    if n_1 * n_2 * n_3 < 0:
        result = "negative"
    elif n_1 * n_2 * n_3 > 0:
        result = "positive"
    elif n_1 * n_2 * n_3 == 0:
        result = "zero"

    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(multiplication(num_1, num_2, num_3))
