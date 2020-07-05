import csv

def csv_write(filename,data):
    with open(filename,'w') as csvfile:
        csv_out=csv.writer(csvfile)
        csv_out.writerow(['name','address','age'])
        for row in data:
            csv_out.writerow(row)




data = [('ram','biratnagar',56), ("hari",'dharan',67),('gopal','abbey road',12)]    
file_name = 'records.csv'

csv_write(file_name,data)