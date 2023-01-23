import csv
from csv import DictWriter

dic=[{"Name":"Messi","Nation":"Argentina"},
     {"Name":"Ronaldo","Nation":"Portugal"},
     {"Name":"Neymar","Nation":"Brazil"}]
     
with open("test.csv",mode="w") as file1:
	filedict=DictWriter(file1,fieldnames=["Name","Nation"])
	filedict.writeheader()
	filedict.writerows(dic)
	
file1.close()

with open("test2.csv",mode="r") as file1:
	csvfile=csv.reader(file1)
	for x in csvfile:
		print(x)
file1.close()
