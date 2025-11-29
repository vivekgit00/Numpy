import numpy as np

# unsorted_array = np.array([64, 34, 25, 12, 22, 11, 90])
# print("Unsorted Array:", unsorted_array)
# sorted_array = np.sort(unsorted_array)
# print("Sorted Array:", sorted_array)

# #2d array sorting
# unsorted_2d_array = np.array([[3, 2, 1], [6, 5, 4]])
# print("Unsorted 2D Array:\n", unsorted_2d_array)
# sorted_2d_array_axis0 = np.sort(unsorted_2d_array, axis=0)
# print("Sorted 2D Array along colomn:\n", sorted_2d_array_axis0, axis=0)
# sorted_2d_array_axis1 = np.sort(unsorted_2d_array, axis=1)
# print("Sorted 2D Array along row:\n", sorted_2d_array_axis1)

# # sorting with indexes
# idx = np.argsort(unsorted_array)
# print("Indexes for Sorted Array:", idx)

# #Descending order
# descending_sorted_array = np.sort(unsorted_array)[::-1]
# print("Sorted Array in Descending Order:", descending_sorted_array)

# # Custom sorting using a key (sorting based on absolute values)
# custom_array = np.array([-3, -1, -2, 4, 0])
# print("Custom Array:", custom_array)
# sorted_custom_array = custom_array[np.argsort(np.abs(custom_array))]
# print("Custom Sorted Array based on Absolute Values:", sorted_custom_array)

# # Stable sort example
# stable_sorted_array = np.sort(unsorted_array, kind='stable')
# print("Stable Sorted Array:", stable_sorted_array)

# # Partial sorting (finding the 3 smallest elements)
# partial_sorted_array = np.partition(unsorted_array, 3)[:3]
# print("3 Smallest Elements:", partial_sorted_array)

# # Lexicographical sorting of structured array
# structured_array = np.array([(1, 'b'), (2, 'a'), (1, 'a')], dtype=[('num', 'i4'), ('char', 'U1')])
# print("Structured Array:", structured_array)

# lex_sorted_array = np.sort(structured_array, order=['num', 'char'])
# print("Lexicographically Sorted Structured Array:", lex_sorted_array)

# # In-place sorting
# inplace_array = np.array([5, 3, 8, 6, 2])
# print("Array before In-place Sort:", inplace_array)

# inplace_array.sort()
# print("Array after In-place Sort:", inplace_array)
# print("Sorted 2D Array along row:\n", sorted_2d_array_axis1)
# print("Sorted 2D Array along colomn:\n", sorted_2d_array_axis0, axis=0)

# # finding the indices that would sort an array
# unsorted_array_2 = np.array([50, 20, 30, 10, 40])
# print("Unsorted Array 2:", unsorted_array_2)
# sorted_indices = np.argsort(unsorted_array_2)
# print("Indices that would sort Array 2:", sorted_indices)


x = np.arange(10)

x[2:7] = 1
print(x)
# x[2:7] = np.arange(5)
# print(x)