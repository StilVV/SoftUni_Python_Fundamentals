quantity = int(input())
days = int(input())

total_spend = 0
total_spirit = 0

ornament_set_price, ornament_set_point = 2, 5
tree_skirt_price, tree_skirt_points = 5, 3
tree_garland_price, tree_garland_points = 3, 10
tree_lights_price, tree_lights_points = 15, 17

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 10 == 0:
        total_spirit -= 20
        total_spend += 23

    if day % 2 == 0:
        total_spend += ornament_set_price * quantity
        total_spirit += ornament_set_point

    if day % 3 == 0:
        total_spend += (tree_garland_price + tree_skirt_price) * quantity
        total_spirit += tree_garland_points + tree_skirt_points

    if day % 5 == 0:
        total_spend += tree_lights_price * quantity
        total_spirit += tree_lights_points
        if day % 3 == 0:
            total_spirit += 30

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_spend}")
print(f"Total spirit: {total_spirit}")
