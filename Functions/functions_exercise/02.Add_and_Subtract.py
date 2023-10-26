def sum_number(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    returned_result = sum_number(first, second)
    final_result = subtract(returned_result, third)
    return final_result


firs_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(firs_number, second_number, third_number))
