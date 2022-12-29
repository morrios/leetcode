#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141-2] 找出环形链表的环起点
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> ListNode:
        p1 = head
        p2 = head
        while(p2 and p2.next):
            p1 = p1.next
            p2 = p2.next.next
            if p1 is p2:
                break
        #如果快指针，为空，或者快指针next为空，则说明没有环
        if p2 is None or p2.next is None:
            return None
        p1 = head
        while(p1 != p2):
            p1 = p1.next
            p2 = p2.next
        return p1

        

        
# @lc code=end

