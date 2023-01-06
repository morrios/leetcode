#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while(fast < len(nums)):
            if nums[fast] != 0:
                slow_t = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = slow_t
                slow = slow + 1
            fast = fast + 1
# @lc code=end

