collection_of_items = input().split("|")
budget = float(input())

TRAIN_TICKET = 150

new_price = 0
total_money = 0
profit = 0
new_prices = []

for cell in collection_of_items:
    is_valid = False
    item, new_price = cell.split("->")
    new_price = float(new_price)
    if item == "Clothes":
        if new_price <= 50:
            is_valid = True
    elif item == "Shoes":
        if new_price <= 35:
            is_valid = True
    elif item == "Accessories":
        if new_price <= 21.50:
            is_valid = True

    if budget >= new_price:
        if is_valid:
            budget -= new_price
            profit += new_price
            new_price = new_price * 1.40
            new_prices.append(new_price)
            total_money += new_price
profit = total_money - profit
total_money += budget

for new_price in new_prices:
    print(f"{new_price:.2f}", end = " ")
print()
print(f"Profit: {profit:.2f}")
if total_money >= TRAIN_TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")

