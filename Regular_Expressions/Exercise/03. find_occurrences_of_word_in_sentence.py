import re

text = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"
matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))

# import re
#
# text = input()
# searched_word = input()
#
# pattern = fr"(?i)\b{searched_word}\b"
# matches = re.findall(pattern, text)
#
# print(len(matches))
