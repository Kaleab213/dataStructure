# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def trav(curr, max_val, min_val):
            if not curr:
                return
            
            if curr != root:
                val = max(abs(max_val-curr.val), abs(min_val-curr.val))
                self.res = max(self.res, val)
            max_val = max(max_val, curr.val)
            min_val = min(min_val, curr.val)

            trav(curr.left, max_val, min_val)
            trav(curr.right, max_val, min_val)
 
        trav(root, float('-inf'), float('inf'))
        return self.res