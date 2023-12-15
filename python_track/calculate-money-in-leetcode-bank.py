class Solution:
    def totalMoney(self, n: int) -> int:
        week = 0
        res = 0
        while n > 0:
            day = 0
            week += 1
            while day < 7:
                if n == 0:
                    break
                res += day+week
                print(res, n, week, day)
                day += 1
                n-=1
        return res
        
