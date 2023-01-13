class rectangle:
	def __init__(self,l,w):
		self.l=l
		self.w=w

	def area(self):
		self.a=self.l*self.w
		print("Area : ",self.a)
.
	def __lt__(self,obj):
		if self.a==obj.a:
			print("They have Same Area")
		else:
			print("They Have Different Area")

obj1=rectangle(12,21)
obj2=rectangle(32,17)
obj1.area()
obj2.area()
obj1<obj2
