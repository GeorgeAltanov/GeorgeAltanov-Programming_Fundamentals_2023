key = int(input())
number_of_lines = int(input())

for i in range(number_of_lines):
    letter = input()

    current_letter = ord(letter) + key
    current_letter = chr(current_letter)

    print(current_letter, end='')
