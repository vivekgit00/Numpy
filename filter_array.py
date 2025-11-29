import numpy as np

arr = np.array([10, 15, 3, 7, 8, 23, 1, 5, 12])
# filtered_arr = arr[arr > 10]
# print("Original Array:", arr)
# print("Filtered Array (elements > 10):", filtered_arr)

# data = arr % 2 == 0
# mask = arr >= 5
# mask = arr % 2 == 0
# mask = arr < 10
# mask = arr % 2 != 0
# print("Mask for :", arr[mask])
# print("Mask for ", arr)

#multiple condition
# mask = (arr > 5) & (arr < 15)
# mask = (arr < 5) | (arr > 20)
# print("Filtered Array with multiple conditions:", arr[mask])
# Using np.where to filter
# indices = np.where(arr > 10) # , arr, 2*arr)
# print("Indices of elements > 10:", indices)
# print("Elements > 10 using np.where:", arr[indices])

#remove value
# arr[arr >= 20]

# 2D array filtering
# arr_2d = np.array([[10, 15, 3], [7, 8, 23], [1, 5, 12]])
# filtered_2d_arr = arr_2d[arr_2d > 10] 
# print("Original 2D Array:\n", arr_2d)
# print("Filtered 2D Array (elements > 10):", filtered_2d_arr)



# using Where
# np.where(condition, true_value, false_value)  

# indices =  [0, 2, 4]
# print("Original Array:", arr[indices])

# where_result = np.where(arr > 10)
# print("Elements > 10 using np.where:", arr[where_result])
# print("Elements > 10 using np.where:", arr[np.where(arr > 10)])
# print("Indices of elements > 10:", where_result)


# condition_one = np.where(arr % 2 == 0, arr, -1)
# print("Elements (even numbers) using np.where:", condition_one)
# print(arr)
# print("Elements value", arr[condition_one])


# np.where 2D array
arr_2d = np.array([[10, 15, 3], [7, 8, 23], [1, 5, 12]])
print(arr_2d)
where_2d_result = np.where(arr_2d >= 10)
print("Original 2D Array:\n", arr_2d[where_2d_result])
print("Indices of elements >= 10 in 2D Array:", where_2d_result)