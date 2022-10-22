from numpy import  *
import numpy as np

x = np.random.rand(3)
print ("random 3 numbers between 1 and 0 rand=>Decimal number")
print(x)

y = np.random.randn(4)
print("\n random 4 numbers but are positiv and negetive randn==>Positive and negative Decimal number")
print(y)

print("\n random 5 integer  numbers between 1 and 5")
z = np.random.randint(1,5)
print(z)

a = np.random.random((3,4))
print("\n create array 2d it has 3 rows and 4 columns")
print (a)

##########randint(start number,end number,numbers of elements array#######
b = np.random.randint(2,100,3)
print("\n create array of 3 numbers betwwen 2 to 100")
print (b)

c = np.random.randint(1,10,(4,5))
print("\n create array 2d it has 4 rows and 5 columns and it has numbers 1-10")
print(c)
