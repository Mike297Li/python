# Input: arr = [5, 4, 1, 2, 3], fn = (x) => x
# Output: [1, 2, 3, 4, 5]
# Explanation: fn simply returns the number passed to it so the array is sorted in ascending order.

def swap(arr,smallestIndex,i):
    temp=arr[i]
    arr[i]=arr[smallestIndex]
    arr[smallestIndex]=temp


arr = [5, 4, 1, 2, 3,8]
i=1
while i<len(arr):
    j=i
    while j>0 and arr[j-1]>arr[j]:
        swap(arr,j-1,j)
        j-=1
    i+=1
print(arr)