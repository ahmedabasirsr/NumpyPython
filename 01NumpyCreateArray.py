from numpy import  *
import numpy as np

list1 = [1,2,3,4]                                      # normally list
x = np.array(list1)                                    # convert list in array
print("Convert list in array ",x)                      # print in format list but its array
print(type(list1),type(x))                             # in view class list and class numpy.array

L=len(x)
#for i in x:  ===>                                     Error does not access first value
#    print(x[i])
'''
for i in range(L):
    print(x[i])
'''


ar =[[11,12,13,14],                                  # list in list===> Array
        [21,22,23,24],
        [31,32,33,34]
    ]
arr2d=np.array(ar)
print("\n convert lists in list to array 2d ")
print(arr2d)



#=================================================================================
#i:numbers of rows. i+5:numbers of columns [7,9,11]: rwos start with 10,20 and 30
#=================================================================================
x = np.array([range (i,i+5) for i in [10,20,30]])
print("\n Creating a two-dimensional array 3x5 and every row start with 10,20 and 30 " )
print(x)

# [range(i=start with 0,number of columns for i in [start first row with 8
#                                                  second row start with 9])
y = np.array([range(i,i+5) for i in [8,9]])
print("\n",y)



#==============================================================================
#i:numbers of rows. i+5:numbers of columns [1,2,3]: rows start with 1,2 and 3
#==============================================================================
y = np.array([range (i,5+i) for i in [80,90,100]])
print("\n Creating a two-dimensional array 3x5 and every columns start with 1,2,3 " )
print(y)

#==============================================================================
#i:numbers of rows. i+5:numbers of columns [1,2,3]: rows start with 1,2 and 3
#==============================================================================
z = np.array([range (i,5+i) for i in range(6)])
print("\n Creating a two-dimensional array 3x4 and every columns start with 1,2,3 " )
print(z)


