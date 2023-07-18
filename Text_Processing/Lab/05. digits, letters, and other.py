single_string = input()

digit = ""
letter = ""
other_character = ""

for ch in single_string:
    if ch.isdigit():
        digit += ch
    elif ch.isalpha():
        letter += ch
    else:
        other_character += ch

print(digit)
print(letter)
print(other_character)
