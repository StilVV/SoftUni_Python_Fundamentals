lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_price = 0
shield_count = 0

for lose in range(1, lost_fights + 1):
    if lose % 2 == 0:
        total_price += helmet_price
    if lose % 3 == 0:
        total_price += sword_price
        if lose % 2 == 0:
            total_price += shield_price
            shield_count += 1
            if shield_count % 2 == 0:
                total_price += armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")
