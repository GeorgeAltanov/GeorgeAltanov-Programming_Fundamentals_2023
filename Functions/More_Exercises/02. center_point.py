# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines.
# Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one.
# The resulting coordinates must be formatted to the lower integer.
#
# Input1:
# 2
# 4
# -1
# 2
#
# Output1: (-1, 2)
#
# Input2:
# 10
# 14.5
# -17.2
# 16
#
# Output2: (10, 14)


from math import floor


def center_point():
    result = ""
    distance_first_point = abs(x1) + abs(y1)
    distance_second_point = abs(x2) + abs(y2)

    if distance_first_point <= distance_second_point:
        result = f"({floor(x1)}, {floor(y1)})"
    else:
        result = f"({floor(x2)}, {floor(y2)})"
    return result


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(center_point())
