
def sorted_list():
    names_list = input().split(", ")
    sorted_names = sorted(names_list, key=lambda x: (-len(x), x))
    return sorted_names


result = sorted_list()
print(result)




# names = input().split(", ")
#
# sorted_list = sorted(names, key=lambda x: (-len(x), x))
#
# print(sorted_list)
