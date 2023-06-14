# You will be given number n. After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters:
# comma ",", period ".", or underscore "_":
# • If a string is pure, print "{string} is pure."
# • Otherwise, print "{string} is not pure!"
#
# Input1:
# 2
# pure string
# not_pure_string
#
# Output2:
# pure string is pure.
# not_pure_string is not pure!
#
# Input2:
# 3
# SoftUni
# 12345
# string.pureness
#
# Output2:
# SoftUni is pure.
# 12345 is pure.
# string.pureness is not pure!



number_of_string = int(input())

for i in range(number_of_string):
    string_pureness = input()

    for symbol in string_pureness:
        if ord(symbol) == 44 or ord(symbol) == 46 or ord(symbol) == 95:
            print(f"{string_pureness} is not pure!")
            break

    else:
        print(f"{string_pureness} is pure.")
