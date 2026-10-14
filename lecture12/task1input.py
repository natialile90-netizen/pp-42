def make_counter(start_value=0):
    count = start_value

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


start = int(input("Enter starting number: "))

counter = make_counter(start)

print(counter())
print(counter())
print(counter())