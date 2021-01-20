import numpy as np
a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])

a0 = np.zeros((2, 2))
print(a0)

a1 = np.ones((1, 2))
print(a1)

c = np.full((2, 2), 7)
print(c)

d = np.eye(3)
print(d)

e = np.random.random((2, 2))
print(e)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[0, 1])

b = a[:2, 1:3]
print(b)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
row_r1 = a[1, :] # row 1, with all the columns
row_r2 = a[1:2, :] # row 1, with all the columns
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)

b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# dot multiplication of 1d arrays
print(v.dot(w))# 9*11 + 10 * 12
print(np.dot(v, w))# 9*11 + 10 * 12
print(np.dot(x,y))