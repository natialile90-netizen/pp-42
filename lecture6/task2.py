inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]

new_items = ["mango," "grape"]

apple_count = inventory.count ("apple")
print(apple_count)

orange_index = inventory.index("orange")
print(orange_index)

inventory.extend(new_items)

print(inventory)

print(inventory[::-1])