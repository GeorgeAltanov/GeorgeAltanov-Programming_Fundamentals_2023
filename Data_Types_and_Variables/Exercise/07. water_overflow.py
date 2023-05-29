number_of_pour = int(input())

capacity_of_tank = 255
total_pour = 0

for i in range(number_of_pour):
    liters_of_pour = int(input())

    if liters_of_pour > capacity_of_tank:
        print("Insufficient capacity!")
        continue

    capacity_of_tank -= liters_of_pour
    total_pour += liters_of_pour

print(total_pour)
