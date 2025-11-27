import numpy as np

# arry = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print("Original Array:", arry)
# print("Sliced Array (indices 2 to 7):", arry[2:8])
# print("with step 2:", arry[2:10:2])
# print("Reversed Array:", arry[::-1])
# print("nagtive step:", arry[8:2:-2])
# print("nagtive step two:", arry[6:-2])
# print("nagtive step:", arry[-2: 6])


arry_2d =  np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20]])

print("Original 2D Array:\n", arry_2d)
print("target element", arry_2d[2, 3])  # Element at 3rd row, 4th column
print("target row", arry_2d[1, :3])    # Entire 2nd row
print("target column", arry_2d[2:,:4])  # Entire 5th column
print("Sliced 2D Array:\n", arry_2d[1:3, 2:5])  # Sub-array from rows 2-3 and columns 3-5

print("First two rows:\n", arry_2d[:2, :])