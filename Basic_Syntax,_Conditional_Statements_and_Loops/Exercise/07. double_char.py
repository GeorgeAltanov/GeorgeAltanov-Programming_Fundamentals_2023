# You will be given strings until you receive the command "End".
# For each string given, you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!
#
# Input1:
# Hello World
# Repeat
# End
#
# Output1:
# HHeelllloo WWoorrlldd
# RReeppeeaatt
#
# Input2:
# 1234!
# SoftUni
# softuni
# End
#
# Output2:
# 11223344!!
# ssooffttuunnii



while True:
    current_string = input()

    if current_string == "SoftUni":
        continue
    if current_string == "End":
        break
    new_string = ""

    for char in current_string:
        new_string += char * 2
    print(new_string)
