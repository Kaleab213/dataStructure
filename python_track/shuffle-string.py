class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        for i in range(len(s)):
            idx = indices.index(i)
            val = s[idx]
            res+=val
        return res
        