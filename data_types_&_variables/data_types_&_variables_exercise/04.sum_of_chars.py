number_of_characters = int(input())
characters_sum = 0

for char in range(number_of_characters):
    character = input()

    characters_sum += ord(character)

print(f"The sum equals: {characters_sum}")
