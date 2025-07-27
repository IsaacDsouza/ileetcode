#110. Balanced Binary Tree. Given a binary tree, determine if it is height balanced.


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced=True

        def height(node):
            nonlocal balanced
            if not node:
                return 0

            left_ht=height(node.left)
            if not balanced:
                return 0
            right_ht=height(node.right)

            if abs(left_ht-right_ht)>1:
                balanced=False
                return 0
            return 1+max(left_ht, right_ht)
        height(root)
        return balanced
        
      

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
print(solution.isBalanced(tree1))