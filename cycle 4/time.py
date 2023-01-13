class time:
	def __init__(self,hr,min,sec):
		self.__hr=hr
		self.__min=min
		self.__sec=sec

	def __add__(self,ob):
		self.__hr+=ob.__hr
		self.__min+=ob.__min
		self.__sec+=ob.__sec
		if(self.__min>=60 or self.__sec>=60):
			if self.__min>=60:
				self.__hr+=int(self.__min//60)
				self.__min=self.__min%60
			if self.__sec>=60:
				self.__min+=int(self.__sec//60)
				self.__sec=self.__sec%60

	def display(self):
		print(f"Time = {self.__hr} Hours {self.__min} Minutes {self.__sec} Seconds")

h=int(input("Enter the hour : "))
m=int(input("Enter the minute : "))
s=int(input("Enter the seconds : "))

ob1=time(h,m,s)
ob1.display()

a=int(input("Enter the hour : "))
b=int(input("Enter the minute : "))
c=int(input("Enter the seconds : "))

ob2=time(a,b,c)
ob2.display()
ob2+ob1
ob2.display()
