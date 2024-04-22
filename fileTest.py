import mysql.connector
import csv

db = mysql.connector.connect()
with open(r'C:\Users\worki\OneDrive\Documents\Coding\Resource Manager\data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        #print(row)
        res = [sub.split('|') for sub in row]
        print(res)
    csv_file.close()

