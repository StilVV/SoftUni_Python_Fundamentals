given_number = input()


def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for digit in number:
        digit = int(digit)
        if digit % 2 != 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f"Odd sum = {even_sum}, Even sum = {odd_sum}"


print(odd_even_sum(given_number))
