import csv

with open("titanic.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    survivors = []

    for passenger in reader:
        if passenger["Survived"] == "1":
            survivors.append(passenger)

    columns = reader.fieldnames

with open("survived.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(survivors)