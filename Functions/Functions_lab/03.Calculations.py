operator = input()
first_number = int(input())
second_number = int(input())


def calculation(operations, first_num, second_num):
    result = None
    if operations == "multiply":
        result = int(first_num * second_num)
    elif operations == "divide":
        result = int(first_num / second_num)
    elif operations == "add":
        result = int(first_num + second_num)
    elif operations == "subtract":
        result = int(first_num - second_num)
    return result


print(calculation(operator, first_number, second_number))
