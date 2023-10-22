deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_of_deck = len(deck) // 2
    left_part = deck[0:middle_of_deck]
    right_part = deck[middle_of_deck:]

    shuffled_deck = []

    for card in range(len(left_part)):
        shuffled_deck.append(left_part[card])
        shuffled_deck.append(right_part[card])

    deck = shuffled_deck

print(deck)
