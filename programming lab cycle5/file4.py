import csv
with open("football.csv",mode="r") as file1:
            file1dict = csv.DictReader(file1)
            for x in file1csv:
                print(x['Name'], x[Nation])