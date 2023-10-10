# Write a program that reads a single string with names separated by comma and space ", ".
# Sort the names by their length in descending order.
# If 2 or more names have the same length, sort them in ascending order (alphabetically).
# Print the resulting list.
#
# Input1: Ali, Marry, Kim, Teddy, Monika, John
#
# Output1: ["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]
#
# Input2: Lilly, Tim, Kate, Tom, Alex
#
# Output2: ['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']


def sorted_list():
    names_list = input().split(", ")
    sorted_names = sorted(names_list, key=lambda x: (-len(x), x))
    return sorted_names


result = sorted_list()
print(result)




# names = input().split(", ")
#
# sorted_list = sorted(names, key=lambda x: (-len(x), x))
#
# print(sorted_list)
