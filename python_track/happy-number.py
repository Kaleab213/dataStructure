class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        while len(n) > 1:
            m = 0
            for i in n:
                m+=int(i)**2
            n = str(m)
        if int(n)==7 or n == "1":
            return True
        return False
