class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for val in s:
            if stack and stack[-1]=="(" and val==")":
                stack.pop()
            else:
                stack.append(val)
        return len(stack)