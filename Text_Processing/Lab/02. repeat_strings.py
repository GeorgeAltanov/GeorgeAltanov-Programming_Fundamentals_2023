data = input().split()
new_text = [word * len(word) for word in data]

print("".join(new_text))


# text = input().split()
# new_text = []
#
# for word in text:
#     new_word = word * len(word)
#     new_text.append(new_word)
# print("".join(new_text))
