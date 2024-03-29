# You are a facility manager at a large business center. One of your responsibilities is to check if each conference room
# in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
# Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors). Keep track of the free chairs:
# • If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# • Otherwise, print: "Game On, {total_free_chairs} free chairs left".
#
# Input1:
# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3
#
# Output1: Game On, 4 free chairs left
#
# Input2:
# 3
# XXXXXXX 5
# XXXX 5
# XXXXXX 8
#
# Output2:
# 1 more chairs needed in room 2
# 2 more chairs needed in room 3


def check_the_rooms(number_of_rooms):
    free_chairs = 0
    needed_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
            needed_chairs += abs(difference)
        else:  # difference >=0:
            free_chairs += difference

    return free_chairs, needed_chairs


count_of_rooms = int(input())
total_free_chairs, total_needed_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")


# 5.1 - Sabina

# def check_the_rooms(number_of_rooms):
#     free_chairs = 0
#     for number_of_room in range(1, number_of_rooms + 1):
#         free_chairs_in_current_room, visitors = input().split()
#         difference = len(free_chairs_in_current_room) - int(visitors)
#         if difference < 0:
#             print(f"{abs(difference)} more chairs needed in room {number_of_room}")
#             free_chairs += difference
#         else:  # difference >=0:
#             free_chairs += difference
#
#     return free_chairs
#
#
# count_of_rooms = int(input())
# total_free_chairs = check_the_rooms(count_of_rooms)
# if total_free_chairs >= 0:
#     print(f"Game On, {total_free_chairs} free chairs left")
