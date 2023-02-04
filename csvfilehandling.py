import csv

"""
# reading csv file
with open("Student_Data.csv", mode="r") as myfile:
    csvfile=csv.reader(myfile)
    for lines in csvfile:
        print(lines)"""

# writing csv file
fields=['name','m1 score','m2 score']
rows=[ ['thriveni','75','73'],
       ['yaswin','74','75'],
       ['varun','67','69'],
       ['rajesh','70','65']]
filename="marks_data.csv"
with open(filename,'w') as file:
    csvwriter=csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)