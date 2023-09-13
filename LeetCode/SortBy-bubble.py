# Input: arr = [5, 4, 1, 2, 3], fn = (x) => x
# Output: [1, 2, 3, 4, 5]
# Explanation: fn simply returns the number passed to it so the array is sorted in ascending order.

def swap(arr,smallestIndex,i):
    temp=arr[i]
    arr[i]=arr[smallestIndex]
    arr[smallestIndex]=temp


arr = [5, 4, 1, 2, 3,8]
for i in range(len(arr)):
    j=0
    while j<len(arr)-1-i:
        if arr[j]<arr[j+1]:
           swap(arr,j,j+1)
        j+=1
print(arr)