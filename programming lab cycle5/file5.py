import csv
dic = [{"Name" : "Messi", "Nation" : "Argentina"},
    {"Name" : "Ronaldo", "Nation" : "Portugal"}
    {"Name" : "Neymar", "Nation" : "Brazil"}]

with open("fb.csv", mode="w") as file1:
    file1Dict=csv.DictWriter(file1, fieldname = ["Name" "Nation"])
    file1Dict.writeheader()
    file1Dict.writerows(dic)
    file1.close()
with open("fb.csv", mode="r") as file2:
    csv file = csv.reader(file2)
    for x in csv file:
        print (x)
file2.close()
