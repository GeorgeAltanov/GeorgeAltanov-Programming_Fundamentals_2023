# Help out the sorting hat to sort the new students in the houses of Hogwarts.
# You will be receiving names until the command "Welcome!". The length of each name determines in which house the student is going:
# • If the name is less than 5 chars, the student is going into Gryffindor
#   o Print "{name} goes to Gryffindor."
# • If the name is exactly 5 chars, the student is going into Slytherin
#   o Print "{name} goes to Slytherin."
# • If the name is exactly 6 chars, the student is going into Ravenclaw
#   o Print "{name} goes to Ravenclaw."
# • If the name is more than 6 chars, the student is going into Hufflepuff
#   o Print "{name} goes to Hufflepuff."
# While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end the program. No more sorting for today!
# If all students are sorted successfully, print "Welcome to Hogwarts."
#
# Input1:
# Harry
# Ron
# Ginny
# Draco
# Welcome!
#
# Output1:
# Harry goes to Slytherin.
# Ron goes to Gryffindor.
# Ginny goes to Slytherin.
# Draco goes to Slytherin.
# Welcome to Hogwarts.
#
# Input2:
# Luna
# Hermione
# Neville
# Voldemort
#
# Output2:
# Luna goes to Gryffindor.
# Hermione goes to Hufflepuff.
# Neville goes to Hufflepuff.
# You must not speak of that name!



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
