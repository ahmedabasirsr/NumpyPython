from numpy import  *
import numpy as np

a = np.array([7,4,1,8,5,2])
print(a)
print("\n print last element",a[-1])
print("\n print from 1 element to 3",a[0:3])
a[0:2]=99
print("\n frist 2 elements are 99: ",a)


x = np.random.randint(1,100,(7,7))
print("\n Create array 2d 7x7 of numbers from 1 to 100 ")
print(x)
print("\n print first element: ",x[0][0])
print ("\n prin 2 row and 3 column: ",x[1][2])
v = x[:,1:2]=99 
print ("\n the second column is 99 ",x)
v = x[1,3]=1000
print ("\n the second row and 4 columns is 1000 ")
print("\n",x)

v = x[0,0:7]=88
print ("\n the first row  is 88 ")
print("\n",x)

v = x[:,-1]=88
print ("\n the last column  is 88 ")
print("\n",x)
'''
