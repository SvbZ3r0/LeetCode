# Two Sum

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        i = 0
        while i < len(nums):
            rem = target - nums[i]
            if rem not in hash_dict:
                hash_dict[nums[i]] = i
            else:
                return [hash_dict[rem], i]
            i += 1