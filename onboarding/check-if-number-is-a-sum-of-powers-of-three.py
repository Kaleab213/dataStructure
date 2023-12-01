class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # dividers = set()
        # while n != 0:
        #     max_pow = int(log(n, 3))
        #     while max_pow >= 0 and max_pow in dividers:
        #         max_pow -=1
        #     if max_pow >= 0:
        #         n -= 3**max_pow
        #         dividers.add(max_pow)
        #     else:
        #         return False
        # return True
        while n > 0:
            if n % 3 == 2:
                return False
            else:
                n //= 3
        return True
