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
