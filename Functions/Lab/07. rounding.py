# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().
#
# Input1: 1.0 2.5 3.0 4.5
# Output1: [1, 2, 3, 4]
#
# Input2: 2.56 1.9 -3.4 8.1
# Output2: [3, 2, -3, 8]


numbers = input().split(" ")

round_list = []
for num in numbers:
    round_list.append(round(float(num)))
print(round_list)
