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