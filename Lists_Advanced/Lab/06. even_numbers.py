# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.
#
# Input1: 3, 2, 1, 5, 8
# Output1: [1, 4]
#
# Input2: 2, 4, 6, 9, 10
# Output2: [0, 1, 2, 4]


number_list = list(map(int, input().split(", ")))

found_indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else "no", range(len(number_list)))

even_indices = list(filter(lambda a: a != "no", found_indices_or_no))

print(even_indices)


# 80%
# def even_numbers():
#     numbers = input().split(", ")
#     numbers = list(map(int, numbers))
#     list_numbers = []
#     indices_even_number = [num for num in numbers if int(num) % 2 == 0]
#     for number in indices_even_number:
#         even_number = numbers.index(number)
#         list_numbers.append(even_number)
#
#     return list_numbers
#
#
# result = even_numbers()
# print(result)
