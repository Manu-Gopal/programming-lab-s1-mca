a=[]
b=[]
a=list(map(int,input("Enter the numbers ").split()))
for x in a:
	if(x>0):
	   b.append(x);

print("The generated list",b)
