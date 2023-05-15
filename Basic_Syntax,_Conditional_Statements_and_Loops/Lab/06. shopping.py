budget = int(input())

while True:
    command = input()

    if command == "End":
        if budget >= 0:
            print("You bought everything needed.")
            break

    command = int(command)
    budget -= command

    if budget < 0:
        print("You went in overdraft!")
        break
