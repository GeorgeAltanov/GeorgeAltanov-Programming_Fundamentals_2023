number_of_messages = int(input())
counter_messages = 0
messages = ""

while counter_messages != number_of_messages:

    number = int(input())
    counter_messages += 1

    if number == 88:
        messages = "Hello"
    elif number == 86:
        messages = "How are you?"
    elif number <= 87:
        messages = "GREAT!"
    elif number > 88:
        messages = "Bye."

    print(f"{messages}")
