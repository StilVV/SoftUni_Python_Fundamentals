first_char = input()
second_char = input()


def characters_in_range(first, second):
    characters_list = []
    for chars in range(ord(first) + 1, ord(second)):
        characters_list.append(chr(chars))
    return characters_list


print(*characters_in_range(first_char, second_char))
