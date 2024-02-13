class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        res = 0
        ones = 0
        if s[0] == "1":
            ones += 1

        for idx in range(1, len(s)):
            if s[idx]=="0":
                res += ones
            else:
                ones += 1
        return res