product = input()
quantity = int(input())
price = 0


def total_price(item, quan):
    if item == "water":
        return f"{quan * 1:.2f}"
    elif item == "coffee":
        return f"{quan * 1.50:.2f}"
    elif item == "snacks":
        return f"{quan * 2:.2f}"
    elif item == "coke":
        return f"{quan * 1.40:.2f}"


print(total_price(product, quantity))
