class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        firp = 0
        secp = 0
        while firp<len(g) and secp<len(s):
            if s[secp]>=g[firp]:
                res += 1
                firp += 1
            secp += 1
        return res
    