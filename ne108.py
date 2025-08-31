#108. Convert Sorted Array to Binary Search Tree. Given an integer array nums where the elements are sorted in ascending order, convert it to a height balanced binary search tree.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def buildbst(left, right):
            if left>right:
                return None
            
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=buildbst(left, mid-1)
            root.right=buildbst(mid+1, right)
            return root
        return buildbst(0, len(nums)-1)
            