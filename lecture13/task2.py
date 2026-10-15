words = ["python", "generator", "yield", "code", "ai", "developer"]

filtered_words = (word.upper() for word in words if len(word) > 4)

for word in filtered_words:
    print(word)