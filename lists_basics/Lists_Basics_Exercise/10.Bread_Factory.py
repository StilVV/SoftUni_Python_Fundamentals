events = input().split("|")

total_energy = 100
total_coins = 100
factory_opened = True

for event in events:
    event_item = event.split("-")
    type_of_event = event_item[0]
    event_value = int(event_item[1])

    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif type_of_event == "order":
        if total_energy < 30:
            total_energy += 50
            print("You had to rest!")
        else:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")

    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            factory_opened = False
            print(f"Closed! Cannot afford {type_of_event}.")
            break

if factory_opened:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
