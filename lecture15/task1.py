def write_quote():
    author = input("Enter your favorite author: ")
    quote = input("Enter a quote: ")

    with open("quotes.txt", "a", encoding="utf-8") as file:
        file.write(f"{author}: {quote}\n")


def read_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        print(file.read())


write_quote()
read_quotes()
