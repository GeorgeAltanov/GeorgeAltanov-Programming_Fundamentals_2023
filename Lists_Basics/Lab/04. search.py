number = int(input())
special_word = input()

my_list = []

for i in range(number):
    current_string = input()
    my_list.append(current_string)

print(my_list)

filtered_strings = []

for current_string in my_list:
    if special_word in current_string:
        filtered_strings.append(current_string)

print(filtered_strings)
