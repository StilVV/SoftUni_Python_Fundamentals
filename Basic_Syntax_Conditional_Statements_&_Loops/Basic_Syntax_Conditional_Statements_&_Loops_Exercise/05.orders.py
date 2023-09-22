orders = int(input())
total = 0

for order in range(orders):
    total_per_day = 0
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    else:
        total_per_day += price_per_capsule * days * capsules_per_day
        total += total_per_day

    print(f"The price for the coffee is: ${total_per_day:.2f}")

print(f"Total: ${total:.2f}")
