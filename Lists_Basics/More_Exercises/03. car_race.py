numbers = [int(s) for s in input().split()]

middle_of_the_deck = len(numbers) // 2
total_time_first_car = 0
total_time_second_car = 0
winner_time = 0
winner_car = ""

left_side = numbers[:middle_of_the_deck]
right_side = numbers[middle_of_the_deck + 1:]
right_side.reverse()
for num in left_side:
    if num == 0:
        total_time_first_car *= 0.80
    total_time_first_car += num

for num in right_side:
    if num == 0:
        total_time_second_car *= 0.80
    total_time_second_car += num

if total_time_first_car < total_time_second_car:
    winner_car = "left"
    winner_time = total_time_first_car
else:
    winner_car = "right"
    winner_time = total_time_second_car

print(f"The winner is {winner_car} with total time: {winner_time:.1f}")
