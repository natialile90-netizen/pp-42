try:

    birth_year = int (input ("enter your birth year : "))
    age = 2026 - birth_year
    print ("your age is" , age)

except ValueError:
    print ("please enter a valid year!")