numbers = input().split(", ")

final_numbers = []
count = 0

for num in range(len(numbers)):
    if numbers[num] != "0":
        final_numbers.append(numbers[num])
        count += 1

zeros = len(numbers) - len(final_numbers)

for zero in range(zeros):
    final_numbers.append("0")

final_numbers = [int(x) for x in final_numbers]
print(final_numbers)
