import numpy as np
import pandas as pd
t = np.array([1,2,3])

print(t)

#no of dimension
print(np.ndim(t))

a = np.array(np.arange(15).reshape(3,5))
print(a)

print(a.shape)
print(a.ndim)
print(a.dtype.name)
# size in bytes 64bites = 8 bytes
print(a.itemsize)
print(a.size)
print(type(a))
print(a[1])
print(a[1,])
# row 1 and all of things in row 1
print(a[1, :])
# all the rows but the col is 2
print(a[:, 2])
print(a[0, 2])
print(a[1, 1:3])

c = np.array([2,3,4])
print(c.dtype.name)
d = np.array([1.2,2.3,3.4])
print(d.dtype.name)
c[1] = 9.5
print(c)
print(c.dtype.name)

g = np.array([[1,2,3], [4,5,6]])
print(g)

print(c)
c = np.array(c, dtype = float)
print(c)
c[1] = 4.5
print(c)

print(np.zeros((3, 4)))


#Exercise 1: Create a 4X2 integer array and Prints its attributes
#* The shape of an array.
#* Array dimensions.
#* The Length of each element of the array in bytes.

#Save your code and output as a screenshot named numpy1.jpeg
print('-' * 30)
x = np.array(np.arange(8).reshape(2,4))
print(x)
print(x.shape)
print(x.ndim)
print(x.itemsize)



print('-' * 30)
sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print("Printing Input Array")
print(sampleArray)
# Exercise 2: Following is the given numpy array return array of odd rows and even columns

row = sampleArray.shape[0]
col = sampleArray.shape[1]
for i in range(row):
    for j in range(col):
        if i % 2 != 0 and j % 2 == 0:
            print(sampleArray[i][j])

print(sampleArray[1:5:2, 0:2:4])
