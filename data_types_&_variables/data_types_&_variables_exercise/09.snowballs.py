number_of_snowballs = int(input())
best_snowball = 0
best_weight = 0
best_time = 0
best_quality = 0

for snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > best_snowball:
        best_snowball = value
        best_quality = quality
        best_time = time
        best_weight = weight

print(f"{best_weight} : {best_time} = {int(best_snowball)} ({best_quality})")
