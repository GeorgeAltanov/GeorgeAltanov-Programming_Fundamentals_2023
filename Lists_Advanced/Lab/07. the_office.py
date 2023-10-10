# You will receive two lines of input:
# • a list of employees' happiness as a string of numbers separated by a single space
# • a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# • If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# • Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"
#
# Input1:
# 1 2 3 4 2 1
# 3
#
# Output1:
# Score: 2/6. Employees are not happy!
#
# Input2:
# 2 3 2 1 3 3
# 4
#
# Output2:
# Score: 3/6. Employees are happy!


def check_employee_happiness():
    happiness_list = list(map(int, input().split(" ")))
    happiness_factor = int(input())

    improve_happiness = [h * happiness_factor for h in happiness_list]

    average_happiness = sum(improve_happiness) / len(improve_happiness)
    happiness_count = sum(h >= average_happiness for h in improve_happiness)
    total_count = len(improve_happiness)

    message = "happy" if happiness_count >= total_count / 2 else "not happy"
    result = f"Score: {happiness_count}/{total_count}. Employeers are {message}!"

    return result


result = check_employee_happiness()
print(result)



# employees_happiness = input().split()
# factor = int(input())
#
# after_mapping = []
# score = 0
# for num in employees_happiness:
#     multiply = int(num) * factor
#     after_mapping.append(multiply)
#     average_happiness = sum(after_mapping) / len(after_mapping)
#
# for n in after_mapping:
#     if n > average_happiness:
#         score += 1
#
# if score >= len(after_mapping) / 2:
#     print(f"Score: {score}/{len(after_mapping)}. Employees are happy!")
#
# else:
#     print(f"Score: {score}/{len(after_mapping)}. Employees are not happy!")
