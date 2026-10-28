phone_book = {
    "Natia": "598 01 02 03",
    "Lile": "555 02 03 04",
    "Leri": "577 04 05 06",
    "Gio": "555 77 55 22",
    "Nini": "555 33 22 11",
}

name = input("Enter name: ")

phone_number = phone_book.get(name)

print("Phone number:", phone_number)
