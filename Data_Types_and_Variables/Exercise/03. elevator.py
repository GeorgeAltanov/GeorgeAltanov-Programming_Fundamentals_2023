# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.
#
# Input1:
# 17
# 3
#
# Output1: 6
#
# Input2:
# 4
# 5
#
# Output2: 1
#
# Input3:
# 10
# 5
#
# Output3: 2



from math import ceil

number_of_people = int(input())
elevator_capacity = int(input())
courses = ceil(number_of_people / elevator_capacity)

print(courses)


# from math import ceil
# number_of_people = int(input())
# capacity = int(input())
#
# courses = number_of_people / capacity
#
# if number_of_people <= capacity:
#     print("All the persons fit inside the elevator.\n"
#           "Only one course is needed.")
# else:
#     print(f"{ceil(courses)}")
