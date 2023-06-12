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
