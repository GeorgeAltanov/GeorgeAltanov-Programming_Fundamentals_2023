stock = {}
while True:
    line = input()

    if line == "statistics":
        break

    product, quantity = line.split(": ")
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity


print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

total_products = len(stock)
total_quantity = sum(stock.values())

print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantity}')