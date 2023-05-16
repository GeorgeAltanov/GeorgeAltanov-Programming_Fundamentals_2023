while True:
    current_string = input()

    if current_string == "SoftUni":
        continue
    if current_string == "End":
        break
    new_string = ""

    for char in current_string:
        new_string += char * 2
    print(new_string)
