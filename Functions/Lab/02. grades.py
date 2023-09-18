# Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
# • 2.00 – 2.99 - "Fail"
# • 3.00 – 3.49 - "Poor"
# • 3.50 – 4.49 - "Good"
# • 4.50 – 5.49 - "Very Good"
# • 5.50 – 6.00 - "Excellent"
#
# Input1: 3.33
# Output1: Poor
#
# Input2: 4.50
# Output2: Very Good
#
# Input3: 2.99
# Output3: Fail


grade_data = float(input())


def solve(grade):
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif 3.00 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    elif 5.50 <= grade <= 6.00:
        return "Excellent"


print(solve(grade_data))
