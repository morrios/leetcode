#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while(prev != tail):
            net = p.next
            p.next = prev
            prev = p
            p = net
        return tail, head


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dumy = ListNode(-1, head)
        pre = dumy
        while(head):
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dumy.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            tail.next = nex
            pre.next = head
            pre = tail
            head = tail.next

        return dumy.next
# @lc code=end

def generate_node(nums):
    # 定义一个哑节点
    p_head = ListNode(-1);
    p = p_head;
    for v in nums:
        temp = ListNode(v);
        p.next = temp;
        p = p.next;
    return p_head.next;

def printList(head: ListNode):
    p = head;
    while(p != None):
        print(p.val)
        p = p.next;
list = generate_node([1,2,3,4,5,6,7,8]);
solution = Solution();
reslut = solution.reverseKGroup(list,3);
printList(reslut)