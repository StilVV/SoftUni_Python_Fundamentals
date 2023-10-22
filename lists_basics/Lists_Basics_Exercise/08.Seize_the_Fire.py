fire_cells = input().split('#')
fire_cells = [x.split(' = ') for x in fire_cells]

water = int(input())

effort = 0
total_fire = 0
cells = []

for type_of_fire, value in fire_cells:
    value = int(value)
    if type_of_fire == 'High':
        if 81 <= value <= 125:
            if water >= value:
                cells.append(value)
                water -= value
                effort += (value * 0.25)

    if type_of_fire == 'Medium':
        if 51 <= value <= 80:
            if water >= value:
                cells.append(value)
                water -= value
                effort += (value * 0.25)

    if type_of_fire == 'Low':
        if 1 <= value <= 50:
            if water >= value:
                cells.append(value)
                water -= value
                effort += (value * 0.25)

print("Cells:")

for x in range(len(cells)):
    print(f" - {cells[x]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells)}")
