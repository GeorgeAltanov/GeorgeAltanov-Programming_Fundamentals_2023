# number = input()
#
# biggest_number = []
#
# for i in number:
#     biggest_number.append(i)
# biggest_number.sort(reverse=True)
# for j in biggest_number:
#     print(j, end='')
number = input()

biggest_number = []

for i in number:
    biggest_number.append(i)
biggest_number.sort(reverse=True)

print(''.join(biggest_number))
