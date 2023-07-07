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
