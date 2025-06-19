#102. Binary Tree Level Order Traversal. Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res=[]
        q= []
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
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
print(solution.levelOrder(tree1))