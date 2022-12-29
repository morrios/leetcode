#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
from ast import List
from typing import Optional
import heapq
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class  node_heap():
    def __init__(self,node):
        self.node = node
    def __lt__(self, other):
        if self.node.val<other.node.val:
            return True
        else:
            return False

class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def mergeKLists(self, lists: List) :
        klist = []
        p = ListNode(-1)
        dump = p
        for v in lists:
            if (v):
                heapq.heappush(klist,node_heap(v))
        while(klist):
            v = heapq.heappop(klist)
            cnode = v.node
            p.next = cnode;
            p = p.next
            if cnode.next:
                heapq.heappush(klist,node_heap(cnode.next))
        return dump.next
        
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
list1 = generate_node([1,4,5]);
list2 = generate_node([1,3,4]);
list3 = generate_node([2,6]);
lists = [list1, list2, list3]
solution = Solution();
reslut = solution.mergeKLists([[]]);
printList(reslut)