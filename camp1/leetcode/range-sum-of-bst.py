# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def recursion(curr):
            if not curr:
                return 
            if curr.val>=low and curr.val<=high:
                self.res += curr.val
            recursion(curr.left)
            recursion(curr.right)
        recursion(root)
        return self.res
