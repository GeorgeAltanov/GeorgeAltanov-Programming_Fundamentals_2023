elements = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    keys = elements[i]
    value = elements[i + 1]
    bakery[keys] = int(value)

print(bakery)
