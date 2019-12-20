import numpy as np
m=input("enter the string in quotes")
o=input("enter the string in quotes")
n=np.array([m,o])
s=np.array(["-","-"])
y=np.core.defchararray.join(s,n)
q=np.char.split(y,sep='-')
p=q
for i in range (0,len(p[1])):
	q[0]=np.append(q[0],p[1][i])
p=np.char.join('',q)
print p[0]
#method 2
c=np.char.array(m)
d=np.char.array(o)
print c+d


