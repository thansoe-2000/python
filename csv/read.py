import csv

with open('people.csv', 'r') as file:
    csvreader = csv.reader(file)
    
    for row in csvreader:
        print(row)
        
    
with open('people.csv', 'r') as file:
    csvreader = csv.DictReader(file)
    
    for row in csvreader:
        print(row["Name"], row["Age"], row["City"])
    