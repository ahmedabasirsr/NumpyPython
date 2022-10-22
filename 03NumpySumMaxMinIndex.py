from numpy import  *
import numpy as np

x = np.random.randint(1,20,7)
print("create array it has numbers from 1 to 10")
print(x)

print("\n Dimension array ",len(x))
print("\n Sorting of array ",sort(x)) 
print("\n sum of array ",sum(x))
print("\n Max of array ",max(x))
print("\n index for max ",x.argmax())
print("\n Min of array",min(x))
print("\n index for min ",argmin(x))
'''
y = np.random.randint(1,100,15)
z = y.reshape(3,5)
print("\n create array 2d from array 1d its has 15 elements")
print(z)      
print("\n index for min ",argmin(z))
print("\n index for max ",argmax(z))
'''
