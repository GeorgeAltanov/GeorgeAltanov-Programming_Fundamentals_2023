number_of_snowballs = int(input())
highest_snowball_value = 0
highest_snowball_weight = 0
highest_snowball_time = 0
highest_snowball_quality = 0

for i in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        highest_snowball_weight = snowball_weight
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality

print(f"{highest_snowball_weight} : {highest_snowball_time} "
      f"= {int(highest_snowball_value)} ({highest_snowball_quality})")
