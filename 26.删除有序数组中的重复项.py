#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lens = len(nums)
        if len == 0:
            return 0
        slow = 0
        fast = 0
        while(fast < lens):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        return slow + 1
        
# @lc code=end

solution = Solution();
list = [1,1,2]
reslut = solution.removeDuplicates([1,1,2]);
for i in range(reslut):
    print(list[i])