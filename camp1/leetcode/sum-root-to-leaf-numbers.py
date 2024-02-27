# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def recursive(prev, curr):
            if not curr:
                return 
                
            prev += str(curr.val)
            if not curr.left and not curr.right:
                self.res += int(prev)
                return 

            recursive(prev, curr.left)
            recursive(prev, curr.right)
        recursive('', root)
        return self.res