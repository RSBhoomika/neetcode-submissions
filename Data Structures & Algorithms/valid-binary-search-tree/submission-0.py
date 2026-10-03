# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, NoDefault0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be strictly within the low and high bounds
            if not (low < node.val < high):
                return False
            
            # Recursively check subtrees:
            # - Left child must be smaller than current node value (updates upper bound)
            # - Right child must be larger than current node value (updates lower bound)
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # Start the recursion with initial boundaries set to negative and positive infinity
        return validate(root, float('-inf'), float('inf'))
        