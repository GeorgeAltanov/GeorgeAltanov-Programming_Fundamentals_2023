list_itself = [int(s) for s in input().split()]
number_k = int(input())

order_of_executions = []
counter = 0
current_index = 0

while len(list_itself) > 0:
    counter += 1
    if counter % number_k == 0:
        order_of_executions.append(list_itself.pop(current_index))
    else:
        current_index += 1

    if current_index >= len(list_itself):
        current_index = 0

print(str(order_of_executions).replace(" ", ""))
