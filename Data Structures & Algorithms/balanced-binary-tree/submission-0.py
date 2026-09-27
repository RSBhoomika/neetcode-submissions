# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkheight(node):
            if not node:
                return 0

            left_ht = checkheight(node.left)
            if left_ht == -1:
                return -1
            right_ht = checkheight(node.right)
            if right_ht == -1:
                return -1

            if abs(left_ht - right_ht)>1:
                return -1

            return max(left_ht,right_ht) + 1
        return checkheight(root) != -1
        