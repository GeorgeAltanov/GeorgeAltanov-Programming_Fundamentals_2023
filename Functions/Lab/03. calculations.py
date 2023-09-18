# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following: "multiply", "divide", "add", "subtract".
#
# Input1:
# subtract
# 5
# 4
#
# Output1: 1
#
# Input2:
# divide
# 8
# 4
#
# Output2: 2


def calculate_result(operator, num_1, num_2):
    result = None
    if operator == "multiply":
        result = num_1 * num_2
    elif operator == "divide":
        result = num_1 // num_2
    elif operator == "add":
        result = num_1 + num_2
    elif operator == "subtract":
        result = num_1 - num_2
    return result

operator = input()
num_1 = int(input())
num_2 = int(input())
print(calculate_result(operator, num_1, num_2))
