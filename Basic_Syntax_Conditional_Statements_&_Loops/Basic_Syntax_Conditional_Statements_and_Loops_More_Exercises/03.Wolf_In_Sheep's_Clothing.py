string = input().split(", ")

for index, item in enumerate(string):
    if index == len(string) - 1:
        if item == "wolf":
            print("Please go away and stop eating my sheep")
    elif item == "wolf":
        wolf_position = len(string) - (index + 1)
        print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!")
        break
