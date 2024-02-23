# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.store = []
        def trav(curr):
            if not curr:
                return
            self.store.append(curr.val)
            trav(curr.right)
            trav(curr.left)
        trav(root)
        self.store.sort()
        return self.store[k-1]
            