# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.
#
# Input1: 3
# Output1:
# *
# **
# ***
# **
# *
#
# Input2: 5
# Output2:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *



num = int(input())

for i in range(1, num + 1):
    print(i * "*")

for i in range(num - 1, 0, -1):
    print(i * "*")
