first_string = input()
second_string = input()
mutated_string = ''

for i in range(len(first_string)):
    formatting_string = first_string[i + 1:]
    mutated_string = second_string[:i + 1] + formatting_string

    if first_string[i] != second_string[i]:
        print(mutated_string)
