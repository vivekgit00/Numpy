import numpy as np

A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

#  access 2D array element
# print(A[1, 2])
# print(A[2, 0])

# #raw access
# print(A[0])
# print(A[1])
# print(A[2, 0:2])
#
# # column access
# print(A[0:2, 1])
print(A[:, 2])
print(A[:, -1])
print(A[0:2, :])
# print(A[:, 1:3])
print("\n", A[1:2, 1:2])

# Slicing
# print(A[0:2, 1:3])