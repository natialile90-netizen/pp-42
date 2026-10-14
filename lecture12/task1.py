def make_counter(start_value=0):
    count = start_value

    def counter():
        nonlocal count
        count +=1
        return count
    return counter

counter = make_counter (start_value=10)

print(counter())

print(counter())