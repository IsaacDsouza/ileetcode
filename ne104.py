#104. Maximum Depth of Binary Tree. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root:Optional[TreeNode])->int:
        if not root:
            return 0
        res = 1
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res,depth)
                #dfs
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
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

tree1 = create_tree_from_list([3,9,20,None,None,15,7])
print(solution.maxDepth(tree1))