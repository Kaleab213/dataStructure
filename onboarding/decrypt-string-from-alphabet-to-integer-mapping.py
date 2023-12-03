class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if i+2<len(s) and s[i+2]=="#":
                val = int(s[i]+s[i+1])
                res += chr(val+96)
                i+=3
            else:
                val = int(s[i])
                res += chr(val+96)
                i+=1
        return res