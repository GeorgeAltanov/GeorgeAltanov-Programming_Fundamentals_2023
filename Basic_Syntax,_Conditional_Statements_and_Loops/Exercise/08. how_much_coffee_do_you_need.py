coffee = 0

while True:
    command = input()
    is_prime = True

    if command == "END":
        break

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee += 1

    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee += 2

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)


# coffee = 0
#
# while True:
#     command = input()
#     is_prime = True
#
#     if command == "END":
#         break
#     if command != "coding" and command != "dog" and command != "cat" and command != "movie" and command != "CODING"\
#             and command != "DOG" and command != "CAT" and command != "MOVIE":
#         continue
#
#     for symbol in command:
#         if 97 <= ord(symbol) <= 122:
#             is_prime = True
#         elif 65 <= ord(symbol) <= 90:
#             is_prime = False
#
#     if is_prime:
#         coffee += 1
#     else:
#         coffee += 2
#
# if coffee > 5:
#     print("You need extra sleep")
# else:
#     print(coffee)
