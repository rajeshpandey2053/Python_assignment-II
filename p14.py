import csv

filename = 'records.csv'
fields = []
rows = []

with open(filename, 'r') as  csvfile:
    csvreader = csv.DictReader(csvfile)
    fields = next(csvreader)
    
    print(fields)
    print(csvreader)
    

    