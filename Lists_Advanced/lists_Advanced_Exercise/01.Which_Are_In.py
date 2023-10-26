first_string = input().split(", ")
second_string = input().split(", ")

final_list = []

for first in first_string:
    for second in second_string:
        if first in second:
            final_list.append(first)
            break

print(final_list)
