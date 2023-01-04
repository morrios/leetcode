#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    #双指针
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        pre = head
        while(pre):
            t = pre.next
            pre.next = cur
            cur = pre
            pre = t
        return cur
    #递归解法
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base
        if(head == None or head.next == None):
            return head
        #递归调用
        last = self.reverseList(head.next)
        #最后
        head.next.next = head
        head.next = None
        return last

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
list = generate_node([2,3,4,5]);
solution = Solution();
reslut = solution.reverseList(list);
printList(reslut)