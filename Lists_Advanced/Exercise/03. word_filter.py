some_text = input().split()
new_list = [word for word in some_text if len(word) % 2 == 0]

print("\n".join(new_list))
