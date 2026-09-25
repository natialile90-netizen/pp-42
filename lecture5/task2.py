n = int(input("Enter a number: "))
total = 0

for number in range(2, n + 1, 2):
    total += number

print(f"The sum of even numbers from 1 to {n} is: {total}")