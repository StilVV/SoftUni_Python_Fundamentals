lines = int(input())

is_balanced = True
open_bracket = False

for chars in range(0, lines):
    line = input()

    if line != '(' and line != ')':
        continue

    is_open_bracket = line == '('

    if open_bracket == is_open_bracket:
        is_balanced = False
        break

    open_bracket = is_open_bracket

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
