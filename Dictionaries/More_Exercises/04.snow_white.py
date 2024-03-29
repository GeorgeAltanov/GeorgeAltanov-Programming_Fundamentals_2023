# Snow White loves her dwarfs, but there are so many, and she doesn't know how to order them.
# Does she order them by name? Or by color of their hat? Or by physics?
# She can't decide, so it's up to you to write a program that does it for her.
# You will be receiving several input lines which contain data about each dwarf in the following format:
# {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
# The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
# You must store the data about the dwarfs in your program. There are several rules though:
# • If 2 dwarfs have the same name but different color, they should be considered different dwarfs, and you should store them both.
# • If 2 dwarfs have the same name and the same color, store the one with the higher physics.
# When you receive the command "Once upon a time", the input ends.
# You must order the dwarfs by physics in descending order and then by total count of dwarfs with the same hat color in
# descending order. Then you must print them all.
# Input
# • The input will consist of several input lines, containing dwarf data in the format, specified above.
# • The input ends when you receive the command "Once upon a time".
# Output
# • As output, you must print the dwarfs, ordered in the way, specified above.
# • The output format is: "({hat_color}) {name} <-> {physics}"
# Constraints
# • The "dwarf_name" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
# • The "dwarf_hat_color" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
# • The "dwarf_physics" will be an integer in range [0, 231 – 1].
# • There will be no invalid input lines.
# • If all sorting criteria fail, the order should be by order of input.
#
# Input1:
# Peter <:> Red <:> 2000
# Teodor <:> Blue <:> 1000
# George <:> Green <:> 1000
# Simon <:> Yellow <:> 4500
# Dopey <:> Simon <:> 1000
# Once upon a time
#
# Output1:
# (Yellow) Simon <-> 4500
# (Red) Peter <-> 2000
# (Blue) Teodor <-> 1000
# (Green) George <-> 1000
# (Simon) Dopey <-> 1000
#
# Input2:
# Grumpy <:> Red <:> 5000
# Grumpy <:> Blue <:> 10000
# Grumpy <:> Red <:> 10000 Happy <:> Blue <:> 10000
# Once upon a time
#
# Output2:
# (Blue) Grumpy <-> 10000
# (Blue) Happy <-> 10000
# (Red) Grumpy <-> 10000

dwarfs = {}

command = input()
while command != "Once upon a time":
    name, color, physics = command.split(" <:> ")
    physics = int(physics)
    dwarfs[color] = dwarfs.get(color, {})
    dwarfs[color][name] = dwarfs[color].get(name, 0)

    if physics > dwarfs[color][name]:
        dwarfs[color][name] = physics

    command = input()

dwarfs_bridge = []

for color in dwarfs:
    for name, points in dwarfs[color].items():
        dwarfs_bridge.append({"hat_color": len(dwarfs[color]), "points": points, "name": name, "color": color})

for info in sorted(dwarfs_bridge, key=lambda x: (-x["points"], -x["hat_color"])):
    print(f"({info['color']}) {info['name']} <-> {info['points']}")
