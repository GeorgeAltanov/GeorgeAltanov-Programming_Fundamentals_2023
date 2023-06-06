level_of_the_fire = input().split("#")
water = int(input())

high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)

fire_out_cells = []
total_fire = 0
effort = 0

for cell in level_of_the_fire:
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    cell_is_valid = False
    if type_of_fire == "High":
        if cell_value in high:
            cell_is_valid = True
    elif type_of_fire == "Medium":
        if cell_value in medium:
            cell_is_valid = True
    elif type_of_fire == "Low":
        if cell_value in low:
            cell_is_valid = True

    if cell_is_valid:
        if water >= cell_value:
            water -= cell_value
            fire_out_cells.append(cell_value)
            total_fire += cell_value
            effort += cell_value * 0.25

print("Cells:")
for fire_out_cell in fire_out_cells:
    print(f"    - {fire_out_cell}")
print("Effort: " f"{effort:.2f}")
print("Total Fire: " f"{total_fire}")
