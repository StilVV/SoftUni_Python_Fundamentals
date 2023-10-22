factor = int(input())
count = int(input())

mult_list = []

for multiplier in range(1, count + 1):
    mult_list.append(factor * multiplier)

print(mult_list)
