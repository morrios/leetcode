#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            need = target - nums[i]
            if need in dic.keys():
                return [dic[need], i]
            dic[nums[i]] = i
        return None
# @lc code=end

