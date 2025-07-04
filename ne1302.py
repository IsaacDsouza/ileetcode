#1302. Deepest Leaves Sum. Given the root of a binary tree, return the sum of values of its deepest leaves. 
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        res=0

        while q:
            res=0
            for _ in range(len(q)):
                node=q.popleft()
                res+=node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return res

solution = Solution()

