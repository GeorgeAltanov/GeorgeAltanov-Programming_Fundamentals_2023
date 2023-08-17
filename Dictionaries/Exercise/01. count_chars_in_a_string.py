# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
# Input1: text
# Output1:
# t -> 2
# e -> 1
# x -> 1
#
# Input2: text text text
# Output2:
# t -> 6
# e -> 3
# x -> 3



symbols = [char for char in input() if char != " "]

letters = {}

for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1

for letter, quantity in letters.items():
    print(f"{letter} -> {quantity}")
