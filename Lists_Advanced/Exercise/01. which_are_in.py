# You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.
#
# Input1:
# arp, live, strong
# lively, alive, harp, sharp, armstrong
#
# Output1: ['arp', 'live', 'strong']
#
# Input2:
# tarp, mice, bull
# lively, alive, harp, sharp, armstrong
#
# Output2: []



#1

first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []
for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)

#1.1

# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# substrings = [first_word for first_word in first_sequence
#               if any(first_word in second_word for second_word in second_sequence)]
# print(substrings)
