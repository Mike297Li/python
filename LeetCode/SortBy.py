# Input: arr = [5, 4, 1, 2, 3], fn = (x) => x
# Output: [1, 2, 3, 4, 5]
# Explanation: fn simply returns the number passed to it so the array is sorted in ascending order.

def swap(arr,smallestIndex,i):
    temp=arr[i]
    arr[i]=arr[smallestIndex]
    arr[smallestIndex]=temp


arr = [5, 4, 1, 2, 3]
for i in range(len(arr)-2):
    smallestIndex=i
    j=i+1
    while j<len(arr):
        if arr[smallestIndex]>arr[j]:
            smallestIndex=j
        j+=1
    swap(arr,smallestIndex,i)

print(arr)