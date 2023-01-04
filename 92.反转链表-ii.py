#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    #迭代
    def __init__(self):
        self.successor = None

    def reverseBetween_diedai(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = None
        dumy = ListNode(-1,head)
        pre = dumy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
            
        return dumy.next
    #递归
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #base
        if(left == 1):
            return self.reverseN(head, right)
        #递归调用
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        #后续处理
        return head
    #翻转链表前N个节点
    
    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #base
        if(n == 1):
            self.successor = head.next
            return head
        #递归
        last = self.reverseN(head.next, n -1)
        head.next.next = head
        head.next = self.successor
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
list = generate_node([1,2,3,4,5,6,7,8]);
solution = Solution();
reslut = solution.reverseBetween(list,2,7);
printList(reslut)