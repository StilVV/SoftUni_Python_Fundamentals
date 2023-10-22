strings = int(input())
magic_word = input()

full_list = []
formatted_list = []

for word in range(strings):
    string = input()

    full_list.append(string)

    if magic_word in string:
        formatted_list.append(string)

print(full_list)
print(formatted_list)
