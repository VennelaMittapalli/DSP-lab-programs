#Appending two array
#method 1
import numpy as np
x=input("Enter the array")
y=input("Enter the another array")
a=np.array(x)
b=np.array(y)
print "A:",a
print "B:",b
l=len(b)
for i in range (0,l):
	a=np.append(a,b[i])
print"Appended array:", a
#method 2
a=input("Enter the array")
b=input("Enter the another array")
print "A:",a
print "B:",b
c=np.append(a,b)
print c

