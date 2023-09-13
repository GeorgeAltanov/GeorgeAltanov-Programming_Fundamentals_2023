# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().
#
# Input1: 6 2 4
# Output1: [2, 4, 6]
#
# Input2: 12 52 11 53 2 8 45
# Output2: [2, 8, 11, 12, 45, 52, 53]


def sorted_numbers(numbers):

    sort_numbers = []
    for n in numbers:
        sort_numbers.append(n)
    sort_numbers = list(map(int, sort_numbers))
    sort_numbers.sort()
    return sort_numbers


numbers = input().split()
print(sorted_numbers(numbers))
