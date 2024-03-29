# LEETCODE - 1. TWO SUM

# BEST:
class Solution:
    """O(n) efficiency: traverse list just once."""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #--Store previously seens nums(keys) and their indexes (vals)
        needed = {}
        #--Iterate candidates:
        for i, num in enumerate(nums):
            #--Give `num`, what other num is needed?
            need = target - num
            #--Have I seen what I need?
            if need in needed:
                return [ needed[need], i ]
            #--Store number and its index
            needed[num] = i
            



# NAIVE APPROACH:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #print(nums, target)
        for i, n in enumerate(nums):
            for j, nn in enumerate(nums):
                if n + nn == target and i != j:
                    #print(n,i,nn,j)
                    return [i,j]




"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Output: Because nums[0] + nums[1] == 9, we return [0, 1].
  Example 2:

  Input: nums = [3,2,4], target = 6
  Output: [1,2]
  Example 3:

  Input: nums = [3,3], target = 6
  Output: [0,1]

Constraints:

  2 <= nums.length <= 104
  -109 <= nums[i] <= 109
  -109 <= target <= 109
  Only one valid answer exists.
"""
