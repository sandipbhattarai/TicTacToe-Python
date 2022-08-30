import csv

with open('data.csv.csv', 'r') as csv_file:
    csv_reader= csv.reader(csv_file)
    next(csv_reader)
    for row_list in csv_reader:
        row=row_list.copy()
        percent =(int(row[4])+122)/100
        print(percent)
        print(row[1],percent,'this is the percent you gain')


