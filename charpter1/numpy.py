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
print(a.itemsize)
print(a.size)
print(type(a))