# Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes.
# He starts by creating a program for only four messages.
# Create a program that receives the n number of messages sent.
# On the following n lines, it will receive integer numbers.
# For each number, the program should print a different message:
# • If the number is 88 - "Hello"
# • If the number is 86 - "How are you?"
# • If the number is not 88 nor 86, and it is below 88 - "GREAT!"
# • If the number is over 88 - "Bye."
#
# Input1:
# 4
# 88
# 86
# 2
# 105
#
# Output1:
# Hello
# How are you?
# GREAT!
# Bye.
#
# Input2:
# 3
# 88
# 88
# 89
#
# Output2:
# Hello
# Hello
# Bye.



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
