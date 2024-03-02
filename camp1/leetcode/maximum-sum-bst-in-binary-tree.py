# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root):
            if not root:
                return True, 0, float('inf'), float('-inf')
            lbst,lsum,lmin,lmax = dfs(root.left)
            rbst,rsum,rmin,rmax = dfs(root.right)
            
            if lbst and rbst and lmax < root.val < rmin:
                self.res = max(self.res,(lsum+root.val+rsum))
                return True, (lsum+root.val+rsum), min(root.val,lmin),max(root.val,rmax)
            else:
                return False,0,0,0
        dfs(root)
        return self.res
        
                