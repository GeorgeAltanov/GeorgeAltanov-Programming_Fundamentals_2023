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
