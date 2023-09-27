# Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even.
# Print each word on a new line.
#
# Input1: kiwi orange banana apple
# Output1:
# kiwi
# orange
# banana
#
# Input2: pizza cake pasta chips
# Output2: cake


some_text = input().split()
new_list = [word for word in some_text if len(word) % 2 == 0]

print("\n".join(new_list))
