from numpy import  *
import numpy as np
x = np.random.randint(1,100,(7,7))
print("\n Create array 2d 7x7 of numbers from 1 to 100 ")
print(x)

v = x[:,-1]=88
print ("\n the last column  is 88 ")
print("\n",x)

v = x[0:7,0]=88 #===> [numbr of rows,number of columns]
print("\n",x)   #===> [0,1]==>first row and second column
                #===> [0:2,0:3]==> for first 3 rows and first 4 columns
v = x[-1,:]=77 #====> last rows is 77
print("\n",x)
v = x[4,3]=999
print("\n",x)
