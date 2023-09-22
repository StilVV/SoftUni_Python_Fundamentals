scope = int(input())
message = ""

for i in range(scope):
    code = int(input())

    if code == 88:
        message = "Hello"
    elif code == 86:
        message = "How are you?"
    elif code == 87 or code < 86:
        message = "GREAT!"
    elif code > 88:
        message = "Buy"

    print(message)
