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
