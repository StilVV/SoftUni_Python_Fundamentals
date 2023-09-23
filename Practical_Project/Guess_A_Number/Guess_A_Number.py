from random import randint
import text

difficulty = int(input(f"{text.welcome}\n\n{text.difficulty}"))
range_of_number = int(input(f"{text.range_of_numbers}"))

tries = 0
wrong = 0
secret_number = 0

match difficulty:
    case 1:
        tries += 20
    case 2:
        tries += 10
    case 3:
        tries += 5

match range_of_number:
    case 1:
        secret_number += randint(0, 100)
    case 2:
        secret_number += randint(0, 1_000)

while True:
    guess_number = int(input("Guess: "))

    if tries == wrong:
        print(f"You did`t guess the number in {wrong} tries.")
        break

    if guess_number > secret_number:
        print(text.too_low)
        wrong += 1
    elif guess_number < secret_number:
        wrong += 1
        print(text.too_high)
    else:
        print(f"Congratulations! "
              f"\nYou guest the number {secret_number} in {wrong + 1} tries ! ! !")
        break
