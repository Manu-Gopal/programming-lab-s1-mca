dict={}
n=int(input("Enter no: of elements in dictionary :"))

for i in range(n):
	key=input("\n Enter the key :")
	value=input("Enter the value :")
	dict[key]=value
as_dict=sorted(dict.items(),reverse=0)
ds_dict=sorted(dict.items(),reverse=1)
print("\n Ascending order :",as_dict)
print("\n Descending order :",ds_dict)
