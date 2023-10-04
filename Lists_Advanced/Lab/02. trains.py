# You will receive a number representing the number of wagons a train has.
# Create a list (train) with the given length containing only zeros.
# Until you receive the command "End", you will receive some of the following commands:
# • "add {people}" – you should add the number of people in the last wagon
# • "insert {index} {people}" - you should add the number of people at the given wagon
# • "leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.
#
# Input1:
# 3
# add 20
# insert 0 15


number_of_wagons = int(input())

train = number_of_wagons * [0]

while True:
    command = input()

    if command == "End":
        break

    command = command.split()

    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        number_of_people = int(command[2])
        train[index] += number_of_people
    elif command[0] == "leave":
        index = int(command[1])
        number_of_people = int(command[2])
        train[index] -= number_of_people

print(train)
