#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums, target):
        num_arr={}
        for i, num in enumerate(nums):
            sum=target-num
            if sum in num_arr:
                return [num_arr[sum],i]
            num_arr[num]=i