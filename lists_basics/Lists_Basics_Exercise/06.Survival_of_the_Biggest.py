start_list = input().split()
number_to_remove = int(input())

list_as_digits = []

for num in start_list:
    list_as_digits.append(int(num))

for num in range(number_to_remove):
    list_as_digits.remove(min(list_as_digits))

print(*list_as_digits, sep=", ")
