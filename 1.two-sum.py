#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        for index, n in enumerate(nums):
            other_no = target - n
            if other_no in nums[index + 1:]:
                return [index, nums.index(other_no, index+1)]
        
# @lc code=end

