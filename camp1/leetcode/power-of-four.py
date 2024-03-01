class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recursive(n):
            if n == 1:
                return True
            elif n<1:
                return False
            return recursive(n/4)
        return recursive(n)