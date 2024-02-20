class Solution:
    def fib(self, n: int) -> int:
        def recursive(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return recursive(n-1) + recursive(n-2)
        return recursive(n)