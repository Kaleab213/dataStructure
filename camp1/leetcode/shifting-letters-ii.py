class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = [0]*(n+1)
        for start, end, direction in shifts:
            if direction:
                dir = 1  
            else:
                dir = -1
            d[start] += dir
            d[end + 1] -= dir
        
        res = ""
        for i in range(n):
            if i != 0: 
                d[i] += d[i - 1]
            new_chr_ascii = (ord(s[i]) - ord("a") + d[i]) % 26 + ord("a")
            res += (chr(new_chr_ascii))
        return res