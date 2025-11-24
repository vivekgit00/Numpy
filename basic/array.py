import numpy as np
import time 
py_list = [1, 2, 3, 4, 5]
# data = py_list * 1
# data = py_list * 2
# data = py_list * 3
# print("Python List:", data)

# np_array = np.array(py_list)
# data = np_array * 3
# print("NumPy Array multiplied by 1:", data)

# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# data = arr_2d * 2
# print("2D NumPy Array multiplied by 2:\n", data)
#
#
## LIST VS NUMPY PERFORMANCE COMPARISON ##
# start_time = time.perf_counter()
# py_list = [i*2 for i in range(10000000)]
# end_time = time.perf_counter()
# print(f"Python list creation time: {end_time - start_time:.6f} seconds")

# start_time = time.perf_counter()
# np_array = np.arange(20000000) * 2 
# end_time = time.perf_counter()
# print(f"NumPy array creation time: {end_time - start_time:.6f} seconds")
# np_array = np.array(py_list)
#
#

#Creating Array From Scratch
# zero = np.zeros((3, 4))
# print("Array of Zeros:\n", zero)

# one = np.ones((2, 5))
# print("Array of Ones:\n", one)

# full = np.full((2,3), 4)
# print("Array Full of 4s:\n", full)

# identity = np.eye(10)
# print("Identity Matrix:\n", identity)

# empty = np.empty((3, 3))
# print("Empty Array:\n", empty)

# range_array = np.arange(10, 50, 5)
# print("Array with Range:\n", range_array)

# linspace_array = np.linspace(0, 1, 5)
# print("Array with Linspace:\n", linspace_array)

# random_array = np.random.random((3, 3))
# print("Random Array:\n", random_array)

seq = np.arange(10)
print("Original Array:", seq)