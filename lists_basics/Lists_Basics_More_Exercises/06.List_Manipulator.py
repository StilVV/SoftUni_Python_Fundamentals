initial_list = [int(x) for x in input().split()]

# Process commands
while True:
    command = input().split()
    action = command[0]

    if action == "end":
        break

    if action == "exchange":
        index = int(command[1])
        if 0 <= index < len(initial_list):
            first_part = initial_list[:index + 1]
            second_part = initial_list[index + 1:]
            initial_list = second_part + first_part
        else:
            print("Invalid index")
    elif action in ("max", "min"):
        parity = command[1]
        if parity == "even":
            elements = [num for num in initial_list if num % 2 == 0]
        else:  # parity == "odd"
            elements = [num for num in initial_list if num % 2 != 0]

        if not elements:
            print("No matches")
        else:
            if action == "max":
                max_element = max(elements)
                max_index = len(initial_list) - 1 - initial_list[::-1].index(max_element)
                print(max_index)
            else:  # action == "min"
                min_element = min(elements)
                min_index = len(initial_list) - 1 - initial_list[::-1].index(min_element)
                print(min_index)
    elif action in ("first", "last"):
        count = int(command[1])
        parity = command[2]
        if count > len(initial_list):
            print("Invalid count")
            continue

        if parity == "even":
            elements = [num for num in initial_list if num % 2 == 0]
        else:  # parity == "odd"
            elements = [num for num in initial_list if num % 2 != 0]

        if not elements:
            print("[]")
        else:
            if action == "first":
                result = elements[:count]
            else:  # action == "last"
                result = elements[-count:]

            print(result)

# Print the final state of the list
print(f"[{', '.join(map(str, initial_list))}]")
