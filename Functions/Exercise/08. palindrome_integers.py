# def character(i):
#     if i == (i[::-1]):
#         return True
#     return False
#
#
# numbers = input().split(", ")
#
# for i in numbers:
#     print(character(i))





def check_palindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    return False


numbers = input().split(", ")
for number in numbers:
    print(check_palindrome(number))

# numbers = input().split(", ")
# is_palindrome = False
#
# for num in numbers:
#     last_num = num[::-1]
#     if num == last_num:
#         is_palindrome = True
#     else:
#         is_palindrome = False
#
#     if is_palindrome:
#         print("True")
#
#     else:
#         print("False")
