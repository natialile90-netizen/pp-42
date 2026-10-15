def even_numbers():
    number = 0

    while True:
        yield number
        number += 2


count = 0

for number in even_numbers():
    print(number)
    count += 1

    if count == 10:
        break