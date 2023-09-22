capacity = 255
full = 0
number_of_flows = int(input())

for flows in range(number_of_flows):
    flow = int(input())

    if full + flow <= capacity:
        full += flow
    else:
        print(f"Insufficient capacity!")

print(full)
