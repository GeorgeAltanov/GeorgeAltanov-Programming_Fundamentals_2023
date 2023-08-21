# Write a program that receives a list of characters separated by ", ". It should create a dictionary with each
# character as a key and its ASCII value as a value. Try solving that problem using comprehension



characters = input().split(', ')
char_dict = {char: ord(char) for char in characters}

print(char_dict)



# characters = input().split(", ")
#
# new_list = {}
# for ch in characters:
#     key = ch
#     value = ord(ch)
#     new_list[key] = int(value)
#
# print(new_list)
