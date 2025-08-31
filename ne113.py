#113. Path Sum II. Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references. A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        res=[]

        def dfs(node, psum, l):
            if not node:
                return 
            
            psum+=node.val
            l.append(node.val)

            if not node.left and not node.right:
                if psum==targetSum:
                    res.append(l[:])
            dfs(node.left, psum, l)
            dfs(node.right, psum, l)
            l.pop()
        dfs(root, 0, [])
        return res


def create_tree_from_list(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


solution = Solution()

tree1 = create_tree_from_list([5,4,8,11,None,13,4,7,2,None,None,5,1])
print(solution.pathSum(tree1, 22))