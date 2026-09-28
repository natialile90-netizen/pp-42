scores = []

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

print (scores)


scores.remove (45)
print (scores)

average = sum(scores)/len(scores)
print (average)


highest = max(scores)
print (highest)

lowest = min(scores)
print(lowest)

scores.sort()
print(scores)


passed_scores = [score for score in scores if score >=60]
print(passed_scores)


