class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    curr_score = 0
                    while stack[-1] != '(':
                        curr_score += stack.pop()
                    stack.pop()
                    stack.append(curr_score * 2)

        while stack:
            score += stack.pop()
        return score