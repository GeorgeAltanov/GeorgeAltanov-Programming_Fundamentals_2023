numbers_of_list = input().split()
number = int(input())

my_list = []

for num in numbers_of_list:
    my_list.append(int(num))
for i in range(number):
    my_list.remove(min(my_list))

print(*my_list, sep=", ")