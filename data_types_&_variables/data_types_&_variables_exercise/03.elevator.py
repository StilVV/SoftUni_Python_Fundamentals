from math import ceil
people = int(input())
capacity = int(input())

elevator_course = ceil(people / capacity)

print(elevator_course)
