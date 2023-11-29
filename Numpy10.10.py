import numpy as np
l=[1,2,3,4,5]
# arr1=np.array([[1,2,3],[4,5,6]])
# print(arr1[0][0])
# 1.shadow copy  ******
arr2=np.array([[[1,2,3],[4,5,6]]])
print(arr2[:,0:1,0:1])
# a=arr2
# arr2[:,0:1,0:1]=100
# print(arr2)
#2.deep copy
# b=arr2.copy()

#3.shape
# arr2 = np.array([[[1, 2, 3], [4, 5, 6]]])
# print(arr2.shape)

# arr3=np.array([1,"2","aa"])
# print(arr3[0])
# 4 zip  ----Creating two lists
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
# #
# # # Combining lists using zip
# zipped_data = zip(names, scores)
#
# # Converting the zip object to a list of tuples
# result = list(zipped_data)
#
# # Printing the result
# print(zipped_data)
# print(type(zipped_data[0]))

# Creating two lists of numbers
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
#
# # Using zip to calculate the sum of corresponding elements
# sums = [x + y for x, y in zip(list1, list2)]
#
# # Printing the result
# print(sums)
# print(type(zip(list1, list2)))

# print(list(np.arange(0.5,5.5)))
# print(list(np.arange(0.5,5.5,0.5)))
# print(list(np.linspace(1,5,10)))
# print(list(np.logspace(1,5)))
# arr5=np.eye(5)
# print(arr5)
#
# print(np.random.rand(2,3))
#
# arr=np.random.randint(1,5,(2,3))
# print(arr)
# arr.reshape(-25,4)
# print(arr)
# 5. slicing 
# arr6=np.array([[4,1,2,1],
#       [2,1,4,1],
#       [4,1,2,4]])
# print(arr6[[0,2],2:])
# print(arr6[[0,1],2:])
# print(arr6[2,1])