from numpy import  *
import numpy as np
x = np.random.randint(1,100,(7,7))
print("\n Create array 2d 7x7 of numbers from 1 to 100 ")
print(x)

v = x[x>70]
print ("\n print array v of  values les then 70")
print(v)
v = x [x%2==0]
print ("\n print array v of  evean values ")
print(v)
v = x [x%2!=0]
print ("\n print array v of  odd values ")
print(v)
