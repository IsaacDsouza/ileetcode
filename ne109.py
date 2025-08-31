#109. Convert Sorted List to Binary Search Tree. Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced binary search tree.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        slow, fast= head, head
        slowp=None

        while fast and fast.next:
            slowp=slow
            slow=slow.next
            fast=fast.next.next
        
        root=TreeNode(slow.val)
        slowp.next=None

        root.left= self.sortedListToBST(head)
        root.right= self.sortedListToBST(slow.next)
        return root
