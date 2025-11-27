import numpy as np

# # Vactor
# vector = np.array([1,2,3,4,5])
# print("Vector:", vector)

# # Matrix 
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("Matrix:\n", matrix)

# # Tensor
# tensor = np.array([[[1,2],[3,4]],
#                    [[5,6],[7,8]],
#                    [[9,10],[11,12]
#                    ]])
# print("Tensor:\n", tensor)

# Array Properties
# arry  = np.array([[1,2,3],[4,5,6], [7,8,9], [10,11,11]], dtype=np.int32)
# print("Array Shape:", arry.shape)
# print("Array Data Type:", arry.dtype)
# print("Array Size:", arry.size)
# print("Array Dimensions:", arry.ndim)
# print("Array Item Size (in bytes):", arry.itemsize)
# print("Array Total Bytes:", arry.nbytes)

arr = np.arange(10, 22)
reshape_arr = arr.reshape(4, 3)
print("Reshaped Array (3x5):\n", reshape_arr)
flattened_arr = reshape_arr.flatten()
print("Flattened Array:", flattened_arr)

revel = reshape_arr.ravel()
print("Raveled Array:", revel)

transponce = reshape_arr.T
print("Transposed Array:\n", transponce)
