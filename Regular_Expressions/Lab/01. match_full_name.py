import re

names = input()
pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
found_correct_names = re.findall(pattern, names)

print(" ".join(found_correct_names))


# import re
#
# names = input()
# pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
#
# matches = re.findall(pattern, names)
#
# for name in matches:
#     print(name, end=' ')