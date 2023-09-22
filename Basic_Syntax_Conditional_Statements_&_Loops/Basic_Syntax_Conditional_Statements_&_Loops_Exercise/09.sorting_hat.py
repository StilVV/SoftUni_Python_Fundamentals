flag = True
while True:
    command = input()

    if command == "Welcome!":
        break
    else:
        name = command

    if name == "Voldemort":
        print("You must not speak of that name!")
        flag = False
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

if flag:
    print("Welcome to Hogwarts.")
