import  matplotlib.pyplot as plt
import numpy as np
l1=int(input("enter the length of x[n]="))
x=np.arange(l1)
print("enter x[n] values=")
for i in range(0,l1):
	x[i]=int(input( ))
n=l1
while (n>=1):
	y[n]=x[n]
n=n-1
print("y[n]=",y)
