#linear algebra applications
import numpy as np
print "..........OPERATIONS ON SINGLE ARRAY......."
a=input("Enter the matrix:")
b=np.array(a)
arr=[np.linalg.matrix_rank(a),np.linalg.matrix_power(a,3),np.trace(a),np.linalg.det(a),np.linalg.inv(a),np.linalg.eig(a),np.diag(a)]
r=["rank","power","trace","determinant","inverse","eigen values","diagonal matrix"]
l=len(arr)
c=0
while(c<l):
	print arr[c],"-----",r[c]
	c+=1
print ".............OPERATIONS ON TWO ARRAYS.........."
d=input("Enter the matrix:")
e=np.array(d)
arr=[np.add(a,b),np.subtract(a,b),np.dot(a,b),np.divide(a,b)]
r=["addtion","subtract","multiplication","dividee"]
l=len(arr)
c=0
while(c<l):
	print arr[c],"-----",r[c]
	c+=1
print ".........SOLTUIONS OF LINEAR EQUATIONS......."
e=input("enter the solution")
f=np.linalg.solve(a,b)
print f

