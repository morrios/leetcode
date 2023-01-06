#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lens = len(nums)
        if lens == 0:
            return 0
        slow = fast = 0
        while(fast < lens):
            if nums[fast] != val:
                nums[slow]  = nums[fast]
                slow = slow + 1

            fast = fast + 1
        return slow
# @lc code=end