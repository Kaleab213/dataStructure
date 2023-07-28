# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recursive(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            left_bst = recursive(node.left, lower, node.val)
            right_bst = recursive(node.right, node.val, upper)

            return left_bst and right_bst

        return recursive(root)
