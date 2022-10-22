from numpy import  *
import numpy as np

x = np.arange(1,11)
print("create array it has numbers from 1 to 10")
print(x)

x = np.arange(1,11,2)
print("\n create array it has numbers from 1 to 10 by step 2")
print(x)

x = np.ones(7)
print("\n create array it has 7 values = 1 ")
print(x)


x = np.ones((7,5))
print("\n create array 2d it has 7x5 values = 1 ")
print(x)

x = np.zeros((4,3))
print("\n create array 2d it has 7x5 values = 0 ")
print(x)

x = np.zeros((70,50))
print("\n create array 2d it has 70x50 values = 0. do not view complet array ...")
print(x)
print ("print dimension array",x.shape)

