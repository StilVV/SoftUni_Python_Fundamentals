list_of_gifts = input().split()
command = input()

while not command == "No Money":
    command = command.split()

    if "OutOfStock" in command:
        for gift in range(len(list_of_gifts)):
            if command[1] in list_of_gifts[gift]:
                list_of_gifts[gift] = "None"

    elif "Required" in command:
        for gift in range(len(list_of_gifts)):
            if gift == int(command[2]):
                list_of_gifts[gift] = command[1]

    elif "JustInCase" in command:
        list_of_gifts[-1] = command[1]

    command = input()

while "None" in list_of_gifts:
    list_of_gifts.remove("None")

print(*list_of_gifts, sep=' ')
