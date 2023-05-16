number_of_string = int(input())

for i in range(number_of_string):
    string_pureness = input()

    for symbol in string_pureness:
        if ord(symbol) == 44 or ord(symbol) == 46 or ord(symbol) == 95:
            print(f"{string_pureness} is not pure!")
            break

    else:
        print(f"{string_pureness} is pure.")
