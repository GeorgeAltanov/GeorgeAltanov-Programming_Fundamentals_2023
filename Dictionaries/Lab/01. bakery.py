# Your first task at your new job is to create a table of the stock in a bakery, and you really don't want to fail on your first day at work.
# You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single
# space (the first element is the key, the second – the value, and so on).
# Create a dictionary with all the keys and values and print it on the console.
#
# Input1: bread 10 butter 4 sugar 9 jam 12
# Output1: {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
#
# Input2: eggs 3 sugar 7 salt 1 butter 3
# Output2: {'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3}


elements = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    keys = elements[i]
    value = elements[i + 1]
    bakery[keys] = int(value)

print(bakery)
