data = input().split()
left_product = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    left_product[key] = int(value)

searched_products = input().split()
for product in searched_products:
    if product in left_product:
        print(f"We have {left_product[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
