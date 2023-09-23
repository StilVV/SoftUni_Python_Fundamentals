key = int(input())
lines = int(input())

decrypted_message = ""

for char in range(lines):
    character = input()

    decrypted_message += chr(ord(character) + key)

print(decrypted_message)
