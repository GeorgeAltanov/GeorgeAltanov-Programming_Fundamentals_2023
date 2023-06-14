# Write a program that takes a single string and prints a list of all the capital letters indices.
#
# Input1: pYtHoN
# Output1: [1, 3, 5]
#
# Input2: CApiTAls
# Output2: [0, 1, 4, 5]




word = input()

list_capital_letters = []

for i in range(len(word)):
    current_letter = ord(word[i])
    if 65 <= current_letter <= 90:
        list_capital_letters.append(i)

print(list_capital_letters)
