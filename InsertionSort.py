def selectionSort(arr):
    for pointer in range(1, len(arr)): # from index 1
        position = pointer
        currentVal = arr[pointer]
        while position > 0 and arr[position - 1] > currentVal:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = currentVal
    return arr


print(selectionSort([2, 1, 3, 9, 8, 5]))
# my_arr=[2,1,3,6,8,5]
# print(len(my_arr))
