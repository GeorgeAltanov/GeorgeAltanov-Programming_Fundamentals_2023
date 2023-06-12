
def sorted_numbers(numbers):

    sort_numbers = []
    for n in numbers:
        sort_numbers.append(n)
    sort_numbers = list(map(int, sort_numbers))
    sort_numbers.sort()
    return sort_numbers


numbers = input().split()
print(sorted_numbers(numbers))
