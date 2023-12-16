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


# %% numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))


print(a < 2)

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[1,2,3], [4,5,6]])

# element wise product
print(a * b)

# matrix product
a.dot(b.T)

print(np.exp(a))

a = np.random.random((5,5))

print(a.sum())
print(a.max())
print(a.min())


print(a.sum(axis=0))
print(a.sum(axis = 1))


print(np.sqrt(a))
print(np.square(a))


np.add(a,a)

# %% indexing and slicing
import numpy as np
array = np.arange(1,8)

print(array[0])

print(array[:4])

reverse_array = array[::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,1])

print(array1[:,1])

print(array1[1,1:4])

print(array1[-1,:])
print(array1[:,-1])




