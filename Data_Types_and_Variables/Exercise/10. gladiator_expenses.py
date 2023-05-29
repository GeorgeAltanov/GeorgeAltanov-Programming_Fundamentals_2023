# lost_fights_count = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# trashed_helmet = 0
# trashed_sword = 0
# trashed_shield = 0
# trashed_armor = 0
# number_of_lost_fights = 0
# expenses = 0
#
# while number_of_lost_fights < lost_fights_count:
#     number_of_lost_fights += 1
#
#     if number_of_lost_fights % 2 == 0:
#         trashed_helmet += 1
#     if number_of_lost_fights % 3 == 0:
#         trashed_sword += 1
#     if number_of_lost_fights % 2 == 0 and number_of_lost_fights % 3 == 0:
#         trashed_shield += 1
#         if trashed_shield % 2 == 0:
#             trashed_armor += 1
#
# expenses = helmet_price * trashed_helmet + sword_price * trashed_sword\
#            + shield_price * trashed_shield + armor_price * trashed_armor
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")

number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmet_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // (2 * 3)
total_armor_broken = total_shield_broken // 2

expenses = total_helmet_broken * helmet_price\
           + total_sword_broken * sword_price\
           + total_shield_broken * shield_price\
           + total_armor_broken * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
