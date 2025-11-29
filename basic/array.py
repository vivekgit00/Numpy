import numpy as np
import time 



########################################
########################################
# Attribute	Meaning
# arr.ndim	number of dimensions
# arr.shape	shape/size (rows, columns)
# arr.size	total elements
# arr.dtype	data type
# arr.itemsize	bytes per element
########################################
########################################


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

# seq = np.arange(10)
# print("Original Array:", seq)

prices = np.array([101.5, 102.3, 103.8, 102.9])
print(prices)
# discounted_prices = prices - prices * 0.50
# print("Discounted Prices:", discounted_prices)
# increased_prices = prices + 5
# print("Increased Prices:", increased_prices) 

# scaled_prices = prices - 5
# print("Scaled Prices:", scaled_prices)

# doubled_prices = prices * 2
# print("Doubled Prices:", doubled_prices)

# divided_prices = prices / 2
# print("Divided Prices:", divided_prices)

# squared_prices = prices ** 2
# print("Squared Prices:", squared_prices)

# mod_prices = prices / prices[0]
# print("Mod Prices:", mod_prices)

# print("Mean Price", np.mean(prices))
# print("std Price", np.std(prices))
# print("sum Price", np.sum(prices))
# print("min Price", np.min(prices))
# print("max Price", np.max(prices))
# print("argmin Price", np.argmin(prices))
# print("diff Price", np.diff(prices))



# def moving_average(arr, window):
#     return np.convolve(arr, np.ones(window)/window, mode='valid')

# prices = np.array([101,102,103,104,105,106])
# ma3 = moving_average(prices, 3)
# print(ma3) 


# data = np.array([[1,2,3],[4,5,6]])
# print(data[1,2])       # 2
# print(data[:,2])       # first column


# Concatinate two arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
concatenated_array = np.concatenate((arr1, arr2), axis=0)  # Concatenate along rows
print("Concatenated Array:\n", concatenated_array)

# Stack horizontally and vertically
stacked_array_h = np.hstack((arr1, arr2))  # Stack horizontally
print("Stacked Horizontally:\n", stacked_array_h)
stacked_array_v = np.vstack((arr1, arr2))  # Stack vertically
print("Stacked Vertically:\n", stacked_array_v)