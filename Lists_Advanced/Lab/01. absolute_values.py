text = input()

vowels = ['a', 'o', 'u', 'e', 'i']
removed_text = [word for word in text if word.lower() not in vowels]

print("".join(removed_text))
