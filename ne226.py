#226. Invert Binary Tree. Given the root of a binary tree, invert the tree, and return its root.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        """Helper method to visualize the tree structure like an actual tree"""
        if not self:
            return "None"
        
        def get_tree_lines(node):
            if not node:
                return [], 0, 0, 0
            
            # Base case: leaf node
            if not node.left and not node.right:
                line = str(node.val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle
            
            # Only right child
            if not node.left:
                lines, n, p, x = get_tree_lines(node.right)
                s = str(node.val)
                u = len(s)
                first_line = (x + 1) * ' ' + s
                second_line = x * ' ' + '/'
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
            
            # Only left child
            if not node.right:
                lines, n, p, x = get_tree_lines(node.left)
                s = str(node.val)
                u = len(s)
                first_line = s
                second_line = u * ' ' + '\\'
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
            
            # Both children
            left, n, p, x = get_tree_lines(node.left)
            right, m, q, y = get_tree_lines(node.right)
            s = str(node.val)
            u = len(s)
            first_line = (x + 1) * ' ' + s + (y + 1) * ' '
            second_line = x * ' ' + '/' + (u + 2) * ' ' + '\\' + (m - y - 1) * ' '
            
            # Pad lines to same length
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            
            # Combine left and right
            gap_size = u + 2
            combined_lines = [first_line, second_line]
            combined_lines += [left_line + gap_size * ' ' + right_line 
                             for left_line, right_line in zip(left, right)]
            
            return combined_lines, n + m + gap_size, max(p, q) + 2, n + u // 2
        
        lines, _, _, _ = get_tree_lines(self)
        return '\n'.join(lines)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Helper function to create a tree from a list (level-order)
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
tree1 = create_tree_from_list([4, 2, 7, 1, 3, 6, 9])
print("Original tree:")
print(tree1)
inverted1 = solution.invertTree(tree1)
print("Inverted tree:")
print(inverted1)
    
