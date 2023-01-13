class rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b

	def area(self):
		self.a=self.l*self.b
		print("Area : ",self.a)
	def peri(self):
		p=2*(self.l+self.b)
		print("Perimeter : ",p)
	def comp(self,obj):
		if self.a==obj.a:
			print("They have Same Area")
		else:
			print("They Have Different Area")
obj1=rectangle(20,15)
obj2=rectangle(25,10)
obj1.area()
obj2.area()
obj1.peri()
obj2.peri()
obj1.comp(obj2)

