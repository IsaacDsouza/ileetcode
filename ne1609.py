#1609. Even Odd Tree. A binary tree is named Even-Odd if it meets the following conditions: The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc. For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right). For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right). Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q=deque()
        q.append((root))
        level=0

        while q:
            qlen=len(q)
            prev=None

            for _ in range(qlen):
                node=q.popleft()
                
                if level%2==0:
                    if node.val%2==0:
                        return False
                    if prev is not None and node.val<=prev:
                        return False
                else:
                    if node.val%2!=0:
                        return False
                    if prev is not None and node.val>=prev:
                        return False
                prev=node.val
                q.append(node.left)
                q.append(node.right)
            level+=1
        return True

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
tree1 = create_tree_from_list([5,4,2,3,3,7])
print(solution.isEvenOddTree(tree1))