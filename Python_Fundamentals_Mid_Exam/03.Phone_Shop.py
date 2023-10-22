phone_list = input().split(", ")

while True:
    command = input().split(" - ")

    if command[0] == "End":
        break

    if command[0] == "Add":
        model = command[1]
        if model not in phone_list:
            phone_list.append(model)

    elif command[0] == "Remove":
        model = command[1]
        if model in phone_list:
            phone_list.remove(model)

    elif command[0] == "Bonus phone":
        old_new = command[1].split(":")
        if old_new[0] in phone_list:
            old_index = phone_list.index(old_new[0])
            phone_list.insert(old_index + 1, old_new[1])

    elif command[0] == "Last":
        if command[1] in phone_list:
            pop_index = phone_list.index(command[1])
            phone_list.pop(pop_index)
            phone_list.append(command[1])

print(", ".join(phone_list))
