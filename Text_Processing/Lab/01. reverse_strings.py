while True:
    incoming_strings = input()

    if incoming_strings == 'end':
        break

    print(f"{incoming_strings} = {incoming_strings[::-1]}")
