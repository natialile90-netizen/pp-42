
def greeter_bot():
    name = yield "Enter your name"

    while True:
        name = yield f"Hello, {name}!"


bot = greeter_bot()

print(next(bot))

while True:
    name = input("Name: ")

    print(bot.send(name))