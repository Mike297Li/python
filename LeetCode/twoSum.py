# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
from typing import List


def findOutPut(nums,outPut,target):
    for i in range(len(nums)):
     for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            outPut.append(i)
            outPut.append(j)
            return outPut


# def twoSum(nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]



def twoSum(nums: List[int], target: int) -> List[int]:
        values = {}
        for index,value in enumerate(nums):
            X=target-value
            if X in values:
                return [values[X],index]
            else:
                values[value]=index

nums = [3,2,4]
target = 6
# result = twoSum(nums, target)

print(twoSum(nums,target))

