def fact(num):
	f=1
	for i in range(1,num+1):
		f=f*i
	return(f)
num=int(input("enter a number"))
factorial=fact(num)
print("factorial of the number is ",factorial)
