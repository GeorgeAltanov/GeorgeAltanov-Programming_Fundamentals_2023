# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format:
# "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique
#
# Input1:
# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals
#
# Output1:
# John - 5622
# Maya - 89
# Lilly - 633
#
# Input2:
# Alex:6:programming basics
# Maria:7:programming basics
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics
#
# Output2:
# Alex - 6
# Maria - 7


students = []
course_to_search = ""

while True:
    student_info = input()

    if ":" not in student_info:
        course_to_search = student_info
        break

    name, ID, course = student_info.split(":")
    students.append({"name": name, "ID": ID, "course": course})

for student in students:
    if course_to_search.startswith(student["course"][0:3]):
        print(f"{student['name']} - {student['ID']}")


# students_dict = {}
# command = input()
# while ":" in command:
#     info = command.split(":")
#     name, id, course = info[0], info[1], info[2]
#     if course not in students_dict:
#         students_dict[course] = {}
#     students_dict[course][id] = name
#     command = input()
#
# course = " ".join(command.split("_"))
# for key, value in students_dict.items():
#     if key == course:
#         for id, name in value.items():
#             print(f'{name} - {id}')
