non_round = input().split()
round_list = []


def rounding(non_rounds: list):
    for num in non_rounds:
        num = float(num)
        rounds = round(num)
        round_list.append(rounds)
    return round_list


print(rounding(non_round))
