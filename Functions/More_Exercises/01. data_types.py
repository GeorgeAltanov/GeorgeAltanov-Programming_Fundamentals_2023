# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# • If the data type is an int, multiply the number by 2.
# • If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# • If the data type is a string, surround the input with "$".
# Print the result on the console.
#
# Input1:
# int
# 5
#
# Output1: 10
#
# Input2:
# real
# 2
#
# Output2: 3.00
#
# Input3:
# string
# hello
#
# Output3: $hello$


def data_types():
    result = ""

    if first_line == "int":
        result = int(second_line) * 2
    elif first_line == "real":
        result = f"{float(second_line) * 1.5:.2f}"
    elif first_line == "string":
        result = "$" + second_line + "$"

    return result


first_line = input()
second_line = input()

print(data_types())

