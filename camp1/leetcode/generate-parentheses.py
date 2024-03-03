class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def recursive(parentheses, curr, left, right):
            parentheses += curr
            if left==n and right==n:
                self.res.append(parentheses)
                return
            if left > right:
                recursive(parentheses, ")", left, right+1)
            if left < n:
                recursive(parentheses, "(", left+1, right)
        recursive("", "(", 1, 0)
        return self.res