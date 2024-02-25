# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive(curr1, curr2):
            if not curr2 or not curr1:
                return 

            if not curr1.left and curr2.left:
                curr1.left = curr2.left
                curr2.left = None

            if not curr1.right and curr2.right:
                curr1.right = curr2.right
                curr2.right = None
            
            if curr1 and curr2:
                curr1.val += curr2.val

            recursive(curr1.left, curr2.left)
            recursive(curr1.right, curr2.right)
        if not root1 and root2:
            root1 = root2
            root2 = None
        recursive(root1, root2)
        return root1