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
