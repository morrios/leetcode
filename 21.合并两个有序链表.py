#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # @lc code=end
        l1 = list1;
        l2 = list2;
        p = ListNode(-1, None);
        dumy = p;
        while(l1 and l2):
            if l1.val > l2.val:
                dumy.next = l2;
                l2 = l2.next;
            else:
                dumy.next = l1;
                l1 = l1.next;
            dumy = dumy.next;
        if (l1):
            dumy.next = l1;
        if(l2):
            dumy.next = l2;
        return p.next;
# @lc code=end

