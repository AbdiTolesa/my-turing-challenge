"""
Problem:
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2

Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
[1,2][3]
Output: 2
"""

def countfrom(nums, k, index):
  result = 0
  subarrs = []

  while(result < k or (result > k and nums[index] <0)):
    result += nums[index]
    subarrs.append(nums[index])
    if index == len(nums)-1:
      break
    index += 1

  if result == k:
    return 1, subarrs
  else:
    return 0, ''

def SubArrayCount(nums,k):
  nums.append(0)
  result = 0
  subarrs = []
  for index, element in enumerate(nums):
    count, subarr = countfrom(nums, k, index)
    result += count
    subarrs.append(subarr)
  print(result)
  # print(subarrs)

print(SubArrayCount([1,2,3,2,1,0,3,5,1,2,6,-1,-1,-1],3))