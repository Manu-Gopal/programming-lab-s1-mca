import csv
with open('football.csv')as file:
	next(file)
	reado=csv.reader(file)
	[print(x) for x in reado]
