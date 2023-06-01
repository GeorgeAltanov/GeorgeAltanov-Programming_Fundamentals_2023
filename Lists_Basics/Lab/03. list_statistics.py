num = int(input())

positives_num = []
negatives_num = []

for i in range(num):
    number = int(input())

    if number >= 0:
        positives_num.append(number)
    else:
        negatives_num.append(number)

print(positives_num)
print(negatives_num)

print(f"Count of positives: {len(positives_num)}")
print(f"Sum of negatives: {sum(negatives_num)}")