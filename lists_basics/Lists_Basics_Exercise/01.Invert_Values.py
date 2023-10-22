string_numbers = input().split(" ")

new_list =[]

for number in string_numbers:
    numbers = -int(number)
    new_list.append(numbers)

print(new_list)
