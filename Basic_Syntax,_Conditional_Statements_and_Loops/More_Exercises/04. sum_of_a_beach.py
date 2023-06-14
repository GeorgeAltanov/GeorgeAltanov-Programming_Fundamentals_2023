# Beaches are filled with sand, water, fish, and sun.
# Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).
#
# Input1: WAtErSlIde
# Output1: 1
#
# Input2: GolDeNSanDyWateRyBeaChSuNN
# Output2: 3
#
# Input3: gOfIshsunesunFiSh
# Output3: 4
#
# Input4: cItYTowNcARShoW
# 0



text = input()
characters = text.lower()

a = characters.count("sand")
b = characters.count("water")
c = characters.count("fish")
d = characters.count("sun")

points = a + b + c + d

print(points)
