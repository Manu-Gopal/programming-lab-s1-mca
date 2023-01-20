f1=open('eg1.txt','r')
f2=open('eg2.txt','w')
l=f1.readlines()
for i in range(len(l)):
	if i%2==0:
		f2.write(l[i])
