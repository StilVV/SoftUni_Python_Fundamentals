command = input()

while command != "End":
    if command != "SoftUni":
        new_word = ""

        for char in command:
            new_word += char * 2

        print(new_word)

    command = input()
