numbers = [int(s) for s in input().split(", ")]
counter = 0

for i in range(len(numbers)-1, -1, -1):
    if numbers[i] == 0:
        numbers.remove(0)
        counter += 1

for count in range(counter):
    numbers.append(0)

print(numbers)