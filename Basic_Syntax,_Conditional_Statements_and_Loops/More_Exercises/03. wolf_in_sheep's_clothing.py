# Wolves have been reintroduced to Great Britain. You are a sheep farmer and are now plagued by wolves who pretend to be sheep.
# Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
# 4 3 2 1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep".
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.
#
# Input1: sheep, sheep, wolf
# Output1: Please go away and stop eating my sheep
#
# Input2: wolf, sheep, sheep, sheep, sheep, sheep
# Output2: Oi! Sheep number 5! You are about to be eaten by a wolf!



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
