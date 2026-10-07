def analyze_text(text, min_length=3, ignore_stopwords=None):
    if ignore_stopwords is None:
        ignore_stopwords = set()

    words = text.split()
    count = 0

    for word in words:
        if len(word) >= min_length and word not in ignore_stopwords:
            count += 1

    return count


text = "Python is very interesting and useful"

print(analyze_text(text))

print(analyze_text(text, 4))

print(analyze_text(
    text,
    min_length=3,
    ignore_stopwords={"and", "is"}
))