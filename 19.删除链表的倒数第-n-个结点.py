#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        knode = ListNode(-1,head)
        snode = knode
        dump = knode
        k = n + 1
        while(k > 0):
            knode = knode.next
            k = k - 1
        while(knode):
            knode = knode.next
            snode = snode.next  
        snode.next = snode.next.next
        return dump.next
# @lc code=end
