class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        left = 0
        right = n-2
        piles.sort()
        res = 0
        while left < right:
            res += piles[right]
            left += 1
            right -= 2
        return res
        