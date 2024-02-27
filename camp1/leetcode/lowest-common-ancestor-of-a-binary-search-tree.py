# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root
        def recursive(curr):
            if not curr:
                return (False, False)

            val1, val2 = recursive(curr.left)
            leftval = val1 or val2
            val3, val4 = recursive(curr.right)
            rightval = val3 or val4

            currval = (curr==p or curr==q)
            if leftval and rightval:
                print(curr.val)
                self.res = curr
                return(False, False)
            if leftval and currval or rightval and currval:
                self.res = curr
                return(False, False)
            if leftval or rightval or currval:
                return (True, False)
            else:
                return (False, False)

        recursive(root)
        return self.res