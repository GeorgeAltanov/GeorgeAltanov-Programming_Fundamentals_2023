word = input()

list_capital_letters = []

for i in range(len(word)):
    current_letter = ord(word[i])
    if 65 <= current_letter <= 90:
        list_capital_letters.append(i)

print(list_capital_letters)
