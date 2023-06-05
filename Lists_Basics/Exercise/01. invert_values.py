list_of_numbers = input().split()

opposite_number = []

for number in list_of_numbers:
    opposite_num = -int(number)
    opposite_number.append(opposite_num)
print(opposite_number)
