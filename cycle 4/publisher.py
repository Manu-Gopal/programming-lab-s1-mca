class publisher:
	def __init__(self,name):
		self.name=name

class book(publisher):
	def __init__(self,name,title,author):
		publisher.__init__(self,name)
		self.title=title
		self.author=author
	def display(self):
		print("Title = ",self.title,"Author = ",self.author)

class python(book):
	def __init__(self,name,title,author,price,page):
		book.__init__(self,name,title,author)
		self.price=price
		self.page=page
	def display(self):
		print(f"Name   : {self.name}\nTitle  : {self.title}\nAuthor : {self.author}\nPrice  : {self.price}\nPages  : {self.page}")

n=input("Enter the name of the publisher : ")
t=input("Enter the title of the book : ")
a=input("Enter the name of the author : ")
pr=input("Enter the book price : ")
p=input("Enter the number of pages of the book : ")

ob=python(n,t,a,pr,p)
ob.display()
