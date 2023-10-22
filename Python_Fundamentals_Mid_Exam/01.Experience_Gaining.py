needed_experience = float(input())
number_of_battles = int(input())

gain_experience = 0

for battle in range(1, number_of_battles + 1):
    experience_from_battle = float(input())

    if battle % 3 == 0:
        experience_from_battle *= 1.15

    if battle % 5 == 0:
        experience_from_battle *= 0.90

    gain_experience += experience_from_battle

    if gain_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break
else:
    print(f"Player was not able to collect the needed experience, "
          f"{needed_experience - gain_experience:.2f} more needed.")
