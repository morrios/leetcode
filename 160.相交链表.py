#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while(p1 is not p2):
            if p1:
                p1 = p1.next
            else:
                p1 = headB;
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB
        #拼接两个链表
        while(l1.next):
            l1 = l1.next
        alast = l1;
        l1.next = l2
        #找到含环链表的起点
        p1 = headA
        p2 = headA
        while(p2 and p2.next):
            p1 = p1.next
            p2 = p2.next.next
            if p1 is p2:
                break
        #如果快指针，为空，或者快指针next为空，则说明没有环
        if p2 is None or p2.next is None:
            alast.next = None
            return None
        p1 = headA
        while(p1 != p2):
            p1 = p1.next
            p2 = p2.next
        alast.next = None
        return p1
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
list1 = generate_node([2,4,6]);
list2 = generate_node([1,5]);
solution = Solution();
reslut = solution.getIntersectionNode(list1, list2);
printList(reslut)