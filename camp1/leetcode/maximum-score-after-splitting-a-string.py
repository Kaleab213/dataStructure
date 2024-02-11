class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        ones = s.count("1")
        currzeros = 0
        for idx in range(len(s)-1):
            if s[idx] == "0":
                currzeros += 1
            res = max(res, currzeros + ones - (idx+1-currzeros))
        return res
