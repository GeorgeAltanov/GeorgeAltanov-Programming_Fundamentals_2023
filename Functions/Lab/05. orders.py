# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
# • coffee - 1.50
# • water - 1.00
# • coke - 1.40
# • snacks - 2.00
# Print the result formatted to the second decimal place.
#
# Input1:
# water
# 5
#
# Output1: 5.00
#
# Input2:
# coffee
# 2
#
# Output2: 3.00


def order(product, returns):
    result = None
    if product == "coffee":
        result = COFFEE * returns
    elif product == "water":
        result = WATER * returns
    elif product == "coke":
        result = COKE * returns
    elif product == "snacks":
        result = SNACKS * returns
    return result


COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00

product = input()
returns = int(input())

print(f"{order(product, returns):.2f}")
