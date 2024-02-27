class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = [root]
        while queue:
            level_values = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr:
                    level_values.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    level_values.append(None)

            if level_values != level_values[::-1]:
                return False

        return True
