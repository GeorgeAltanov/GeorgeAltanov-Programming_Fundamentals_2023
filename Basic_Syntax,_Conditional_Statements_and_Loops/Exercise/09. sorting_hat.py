name = input()

while name != "Welcome!":
    place = ""

    if name == "Voldemort":
        break
    if len(name) < 5:
        place = "Gryffindor"
    elif len(name) == 5:
        place = "Slytherin"
    if len(name) == 6:
        place = "Ravenclaw"
    if len(name) > 6:
        place = "Hufflepuff"
    print(f"{name} goes to {place}.")
    name = input()

if name == "Voldemort":
    print("You must not speak of that name!")

else:
    print("Welcome to Hogwarts.")


# while True:
#     name = input()
#     place = ""
#
#     if name == "Welcome!":
#         break
#
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         break
#
#     if len(name) < 5:
#         place = "Gryffindor"
#     elif len(name) == 5:
#         place = "Slytherin"
#     if len(name) == 6:
#         place = "Ravenclaw"
#     if len(name) > 6:
#         place = "Hufflepuff"
#
#     print(f"{name} goes to {place}.")
#
# if name != "Voldemort":
#     print("Welcome to Hogwarts.")