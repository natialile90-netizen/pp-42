import csv

with open("ssl_companies.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    companies = []

    for company in reader:
        if int(company["Number of employees"]) > 1000:
            companies.append(company)

with open("sorted_companies.csv", "w", newline="", encoding="utf-8") as file:
    columns = ["Name", "Industry", "Number of employees"]
    writer = csv.DictWriter(file, fieldnames=columns)

    writer.writeheader()

    for company in companies:
        writer.writerow({
            "Name": company["Name"],
            "Industry": company["Industry"],
            "Number of employees": company["Number of employees"]
        })
