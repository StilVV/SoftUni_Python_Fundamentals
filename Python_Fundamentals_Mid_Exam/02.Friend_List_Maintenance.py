friend_list = input().split(", ")

blacklisted = 0
lost = 0

while True:
    command = input().split()

    if command[0] == "Report":
        break

    if command[0] == "Blacklist":
        if command[1] in friend_list:
            index_name = friend_list.index(command[1])
            friend_list[index_name] = "Blacklisted"
            print(f"{command[1]} was blacklisted.")
            blacklisted += 1
        else:
            print(f"{command[1]} was not found.")

    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(friend_list):
            if friend_list[index] == "Blacklisted" or friend_list[index] == "Lost":
                continue
            else:
                print(f"{friend_list[index]} was lost due to an error.")
                friend_list[index] = "Lost"
                lost += 1

    elif command[0] == "Change":
        index_to_change = int(command[1])
        if 0 <= index_to_change < len(friend_list):
            current_name = friend_list[index_to_change]
            new_name = command[2]
            print(f"{current_name} changed his username to {new_name}.")
            friend_list[index_to_change] = command[2]

print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(" ".join(friend_list))
