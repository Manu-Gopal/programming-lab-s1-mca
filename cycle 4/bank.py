class bank:

	def __init__(self,acc_no,name,type_acc):
		self.acc_no=acc_no
		self.name=name
		self.type_acc=type_acc
		self.bal=0

	def deposit(self):
		money=int(input("Enter the amount to deposit:"))
		self.bal=self.bal+money
		print("Money deposited successfully.\nCurrent Balance = ",self.bal)

	def withdraw(self):
		w=int(input("Enter the amount to withdraw:"))
		if w>self.bal:
			print("Insufficient Balance")
		else:
			self.bal=self.bal-w
			print("Withdrawal Succesful.\nCurrent Balance = ",self.bal)

	def menu(self):
		print(" 1. Deposit\n 2. Withdraw\n 3. Exit")
		n=int(input("Enter your choice"))
		return n

nmbr=int(input("Enter the account number : "))
name=input("Enter name : ")
typ=input("Enter account type : ")

ob1=bank(nmbr,name,typ)
a=ob1.menu()

while(a<4):
	if(a==1):
		ob1.deposit()
		a=ob1.menu()
	if(a==2):
		ob1.withdraw()
		a=ob1.menu()
	if(a==3):
		exit()
	
	
