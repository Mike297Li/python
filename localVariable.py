from array import array

# Create an array of integers
# The first argument ('i') specifies the type code for integers
# 'i' indicates that the array will store signed integers
my_array = array('i', [1, 2, 3, 4, 5])

print("Original array:", my_array)
print("Original array0:", my_array[0])
# Modify the first element of the array
my_array[0] = 100

print("Modified array:", my_array)