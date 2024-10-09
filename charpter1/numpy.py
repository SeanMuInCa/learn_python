import numpy as np

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