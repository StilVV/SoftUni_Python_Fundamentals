upper_limit = int(input())
lower_limit = int(input())

for char in range(upper_limit, lower_limit + 1):
    print(f"{chr(char)}", end=" ")
