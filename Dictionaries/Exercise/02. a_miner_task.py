resource = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break

    current_quantity = int(input())

    if current_resource not in resource.keys():
        resource[current_resource] = 0
    resource[current_resource] += current_quantity

for product, quantity in resource.items():
    print(f"{product} -> {quantity}")
