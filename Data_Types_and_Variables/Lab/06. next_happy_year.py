# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.
#
# Input1: 8989
# Output1: 9012
#
# Input2: 1001
# Output2: 1023


year = int(input())

while True:
    year += 1
    year_str = str(year)

    if len(year_str) == len(set(year_str)):
        break

print(year_str)
