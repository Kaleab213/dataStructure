class Solution:
    def reverseWords(self, s: str) -> str:
        newlist = s.split()
        n = len(newlist)
        res = ""
        for i in range(n-1, -1, -1):
            res+=newlist[i]
            if i != 0:
                res+=" "
        return res
        