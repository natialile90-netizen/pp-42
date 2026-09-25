password = ""
tries = 0


while password != "1234" and tries < 3:
    password = input("Enter your 4-digit PIN:  ")
    tries += 1

    if password == "1234":
        print("Access granted!")
        break

    print(f"Incorrect PIN. Remaining attempts: {3 - tries}")

if password != "1234":
    print("Card blocked!")