import numpy as np

arr = np.array([10, 15, 20, 25, 30, 35, 40,4])
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr.shape)
# print(arr.ndim)
# # arr = np.array([1, 2, 3, 4], ndim=2)
# print(arr[-1])
# print(arr[1:3])
# print(arr[1:4:2])
# print(arr[::2])
# arr2 = np.array([1.0, 2.0, 3.0])
# print(arr2.dtype)
# newArr=arr2.astype(int)
# print(newArr.dtype)
# print(newArr.view())
# print(arr.shape)
# newarr = arr.reshape(2,4)
# print(newarr)
#
# arr3 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
#
# newarr = arr3.reshape(-1)
# print(newarr)
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1,arr2))
# print(arr)
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
#
# x = np.where(arr == 4)
# print(x)
# arr = np.array([3, 2, 0, 1])
#
# x = np.sort(arr)[::-1]
# print(x)
# arr[0:3] = 100
# print(arr)
# arr = np.array([1, 2, 3, 4], dtype='U')
#
# print(arr)
# print(arr.dtype)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr2=arr.copy()
# arr2[0][0]=9
# print(arr2)
# #arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(arr.ndim)

# original_array = np.array([1, 2, 3, 4, 5,6])
#
# # Create a view of the original array
# view_array = original_array[1:4]  # This creates a view that includes elements 2, 3, and 4
#
# # Print the original array
# print("Original Array:", original_array)
#
# # Print the view array
# print("View Array:", view_array)
#
# # Modify an element in the view
# view_array[0] = 99
#
# # Print the original array again
# print("Original Array (after modifying the view):", original_array)
# view2=original_array.reshape(2,3)
# view2[0][0]=3
# print(original_array)
# original_array = np.array([[1, 2, 3], [4, 5, 6]])
#
# # Create a view of the original array by transposing it
# view_array = original_array.T
#
# # Print the original array
# print("Original Array:")
# print(original_array)
#
# # Print the view array
# print("View Array (created by transposing):")
# print(view_array)

# original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# # Split the array into three sub-arrays
# sub_arrays = np.split(original_array, 3)
# print(sub_arrays)
# arr = np.array([1,2,3])
# print(np.cumsum(arr))





