import csv
with open("football.csv",mode="r") as file1:
            file1csv = csv.DictReader(file1)
            for x in file1csv:
                print(x["Name"])
