word = input()

final_list = []

for char in range(len(word)):
    if word[char].isupper():
        final_list.append(char)

print(final_list)
