def data_types():
    result = ""

    if first_line == "int":
        result = int(second_line) * 2
    elif first_line == "real":
        result = f"{float(second_line) * 1.5:.2f}"
    elif first_line == "string":
        result = "$" + second_line + "$"

    return result


first_line = input()
second_line = input()

print(data_types())

