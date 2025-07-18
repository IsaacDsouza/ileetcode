#112. Path Sum. Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curSum):
            if not node:
                return False
            curSum+=node.val
            if not node.left and node.right:
                return curSum==targetSum
            return (dfs(node.left, curSum),dfs(node.right, curSum))
        return dfs(root, 0)

