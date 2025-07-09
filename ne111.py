#111. Minimum Depth of Binary Tree

from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q=deque()
        q.append((root,1))

        while q:
            node, depth = q.popleft()

            if not node.left and node.right:
                return depth
            
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))


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

tree1 = create_tree_from_list([2,None,3,None,4,None,5,None,6])
print(solution.minDepth(tree1))