import csv

rows = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    # print(next(reader))
    
    for row in reader:
        # Create full_name column
        row["full_name"] = row["name"] + " " + row["surname"]
        rows.append(row)


# Get all column names
fieldnames = rows[0].keys()

# Write updated data to new file
with open("updated_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(rows)