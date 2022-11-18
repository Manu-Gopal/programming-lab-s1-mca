 def listSum(numbers) :
	sum=0
	for element in numbers :
		sum+=element
	print(f"sum of all elements in the list : {sum}")

numbers=input("enter elements with each element separated by space :").split()
numbers=list(map(int,numbers))
listSum(numbers)
