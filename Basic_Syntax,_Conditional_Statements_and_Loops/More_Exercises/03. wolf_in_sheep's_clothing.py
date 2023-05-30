animals = input()
my_list = animals.split(", ")

counter = 0

if my_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
    exit()

for i in my_list[::-1]:
    if i == "sheep":
        counter += 1
    if i == "wolf":
        print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
