# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def recursive(curr, col, row):
            if not curr:
                return

            self.res.append([col, row, curr.val])

            recursive(curr.left, col-1, row+1)
            recursive(curr.right, col+1, row+1)

        recursive(root, 0, 0)
        self.res.sort()

        ans = []
        tempo = []
        for idx in range(len(self.res)):

            if tempo and self.res[idx-1][0]!=self.res[idx][0]:
                ans.append(tempo)
                tempo = []

            tempo.append(self.res[idx][2]) 
        ans.append(tempo)
        return ans
