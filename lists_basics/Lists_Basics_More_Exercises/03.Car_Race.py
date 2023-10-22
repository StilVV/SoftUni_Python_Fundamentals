cars = input().split()

middle = int(len(cars) / 2)
left = 0
right = 0
cars = [int(x) for x in cars]

for car in range(middle):
    if cars[car] == 0:
        left *= 0.8
    left += cars[car]

for car_b in cars[:middle:-1]:
    if car_b == 0:
        right *= 0.8
    right += car_b

if left < right:
    print(f"The winner is left with total time: {left:.1f}")
else:
    print(f"The winner is right with total time: {right:.1f}")
