words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]
word_counts = {}

for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

print (word_counts)

for w, count in word_counts.items():
    if count >1:
        print (w)