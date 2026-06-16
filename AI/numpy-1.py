# NumPu bu library va bu raqamlar bilan ishlash uchun kutubxona xisoblanadi
# pip install numpy - install
# ndarraylarda hamma arraylarning length bir xil bo'lishi kerak bo'lmasam dimensions.
# shape ning ikkiy qiymati birinchisi arraylar soni ikkinchisi array length hisoblanadi
import numpy as np

arr = np.array([1, 5, 4, 7])

print("arr:", arr)


arr2d = np.array([[1, 5, 4, 7], [5, 7, 8, 4]])

print("arr2d:", arr2d)

arr3d = np.array([[1, 5, 4, 7], [5, 7, 8, 4], [8, 9, 7, 2]])
arr_shape = arr3d.shape
print("arr3d:", arr_shape)


# dtype

a = np.array([1, 2, 3, 8, 7, 8, 9, 7])
print(a.dtype)

# reshape
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print("shaped_array:", b)


# astype
a = np.array([1, 2, 3])
b = a.astype(float)
print("astype:", b)

# np.zeros(), np.ones() => dummy data

z = np.zeros((2, 3))
o = np.ones((2, 3))

print("zeros", z)
print("ones", o)

# ndim
a = np.array([[1, 2], [2, 2]])
print("ndim:", a.ndim)

# arange()

a = np.arange(1, 7)
print("arange:", a)

# sum(), min(), max(), mean()


# flaatten()

a = np.array([[1, 2], [3, 4]])
print("flaatten:", a.flatten())

# T => transpose
a = np.array([[1,2], [3,4]])
print("transpose", a.T)

#dot() @ shunday method bilan ham ishlatishar ekan

a = np.array([[1,2], [3,4]])
b= np.array([[1,5], [3,8]])

print("dot/multiplication:", a.dot(b))

# random.rand

a = np.random.rand(2,3)
print("random rand:", a)