num = float(input())

if num > 0:
    if 0 < num < 1:
        print("small positive")
    elif 1 <= num < 1_000_000:
        print("positive")
    elif num > 1_000_000:
        print("large positive")

elif num < 0:
    if 1 <= abs(num) < 1_000_000:
        print("negative")
    elif 0 < abs(num) < 1:
        print("small negative")
    elif abs(num) > 1_000_000:
        print("large negative")

else:
    print("zero")
