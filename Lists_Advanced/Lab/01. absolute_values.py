# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
#
# Input1: Python
# Output1: Pythn
#
# Input2: ILovePython
# Output2: LvPythn


text = input()

vowels = ['a', 'o', 'u', 'e', 'i']
removed_text = [word for word in text if word.lower() not in vowels]

print("".join(removed_text))
