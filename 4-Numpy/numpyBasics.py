# importing
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1*5 vector

print(array.shape)

a = array.reshape(3,5)
print(a.shape)
print(a.ndim)

print("data type: ", a.dtype.name)
print(a.size)

print(type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

zeros = np.zeros((3,4))
zeros[0,0] = 5
print(zeros)

np.ones((3,4))

np.empty((2,3))

a = np.arange(10,50,5 )
print(a)

a = np.linspace(10, 50,20)
print(a)