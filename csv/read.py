import csv

# Open and read the CSV file
with open('people.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    for data in csv_reader:
        print(data)
        
    
with open('people.csv', mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        print(row)
        

with open('writer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No', 'Name', 'Address'])
    writer.writerow([1, 'TTs', 'Png'])
    writer.writerow([2, 'Mra Pann', 'PT'])

with open('writer.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        print(row)
    

    
        

    
    
