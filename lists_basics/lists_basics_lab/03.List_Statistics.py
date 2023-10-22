range_numbers = int(input())

positive_list = []
negative_list = []

for num in range(range_numbers):
    number = int(input())

    if number < 0:
        negative_list.append(number)
    else:
        positive_list.append(number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
range_numbers = int(input())

positive_list = []
negative_list = []

for num in range(range_numbers):
    number = int(input())

    if number < 0:
        negative_list.append(number)
    else:
        positive_list.append(number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
